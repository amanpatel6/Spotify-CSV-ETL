import pandas as pd

# Extract
def extract(csv):
    df = pd.read_csv(csv)
    
    return df
# pd.set_option('display.max_columns', None) - this is how you show ALL columns in terminal when you print

# Transform
def transform(df):
    columns_to_keep = ["track_name", "artist_name", "album_name", "duration_ms", "explicit", "genre"]

    df1 = df[columns_to_keep]

    updated_column_names = {    
        "track_name" : "song",
        "artist_name" : "artist",
        "album_name" : "album",
        "duration_ms" : "duration"
    }

    df2 = df1.rename(columns=updated_column_names)

    pd.set_option('display.max_columns', None)

    # print(df2.isnull().sum()) # shows the sum of nulls in each column

    df3 = df2.dropna() # drops ALL null values in the dataframe

    df3["duration"] = df3["duration"] / 1000 # converting from ms to s
    df3['duration'] = df3['duration'].apply(lambda x: f"{int(x // 60):02d}:{int(x % 60):02d}") # converting to MM:SS format

    df3["explicit"] = df3["explicit"].str.capitalize() #.str as this is used for a SERIES of strings
    df3["explicit"] = df3["explicit"].replace({"No" : "False", "Yes" : "True"}) # converts yes and no to True and False

    return df3

# LOAD
def load(df3):
    df3.to_csv("cleaned_data.csv", index=False)

df = extract("mock_spotify_noisy_dataset.csv")
df3 = transform(df)
load(df3)
