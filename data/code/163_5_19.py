import pandas as pd

class FruitColorMapper:
    FRUIT_COLORS = {
        "Apple": "Red",
        "Banana": "Yellow",
        "Cherry": "Red",
        "Date": "Brown",
        "Elderberry": "Purple"
    }

    @staticmethod
    def create_dataframe():
        data = {"Fruit": list(FruitColorMapper.FRUIT_COLORS.keys()), "Color": list(FruitColorMapper.FRUIT_COLORS.values())}
        return pd.DataFrame(data)

if __name__ == '__main__':
    df = FruitColorMapper.create_dataframe()
    print(df)