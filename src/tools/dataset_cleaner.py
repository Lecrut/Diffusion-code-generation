import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("data/dataset.csv")

    print(df['valid'].value_counts())
    
    # invalid_indexes = df[df['valid'] == True]

    # pd.DataFrame(invalid_indexes).to_csv("data/dataset.csv", index=False)

