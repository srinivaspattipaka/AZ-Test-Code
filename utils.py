import pandas as pd

COLUMN_NAMES = [
    "tid", "price", "dateOfTransfer", "postcode", "propertyType", "isNewProperty",
    "tenure", "paon", "saon", "street", "locality", "city", "district", "county",
    "ttype", "recordStatus"
]


def load_all_data(start=1995, end=2021):
    all_dfs = []
    for year in range(start, end + 1):
        url = f"http://prod.publicdata.landregistry.gov.uk.s3-website-eu-west-1.amazonaws.com/pp-{year}.csv"
        df = pd.read_csv(url, header=None, names=COLUMN_NAMES)
        df["year"] = pd.to_datetime(df["dateOfTransfer"]).dt.year
        df["pc_left"] = df["postcode"].str.split().str[0]
        all_dfs.append(df)
    return pd.concat(all_dfs, ignore_index=True)