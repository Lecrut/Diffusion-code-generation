import pandas as pd

class FruitColorMapper:
    FRUITS = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
    COLORS = ["Red", "Blue", "Green", "Yellow", "Purple"]

    @staticmethod
    def map_fruits_to_colors(fruits, colors):
        result = []
        for fruit in fruits:
            first_letter = fruit[0].lower()
            for color in colors:
                if color[0].lower() == first_letter:
                    result.append((fruit, color))
        return pd.DataFrame(result, columns=["Fruit", "Color"])

if __name__ == '__main__':
    mapper = FruitColorMapper()
    df = mapper.map_fruits_to_colors(FruitColorMapper.FRUITS, FruitColorMapper.COLORS)
    print(df)