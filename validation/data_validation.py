import pandas as pd

def validate_dataset(df):
    print("========== DATA VALIDATION REPORT ==========\n")

    print("Dataset Shape:", df.shape)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:", df.duplicated().sum())

    if not df["Year"].is_monotonic_increasing:
        print("\nWarning: Dataset is not sorted by Year!")

    if (df["Production"] < 0).any():
        print("\nWarning: Negative production values detected!")

    print("\nProduction Summary Statistics:")
    print(df["Production"].describe())

    print("\n============================================\n")
