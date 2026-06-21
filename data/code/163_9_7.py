class FruitColorMerger:
    FRUIT_COLOR_PAIRS = {
        "apple": "red",
        "banana": "yellow",
        "grape": "purple",
        "orange": "orange"
    }

    @staticmethod
    def merge_pairs(pairs):
        result = {}
        for fruit, color in pairs.items():
            if fruit not in result:
                result[fruit] = color
        return result

if __name__ == '__main__':
    merger = FruitColorMerger()
    merged_dict = merger.merge_pairs(FruitColorMerger.FRUIT_COLOR_PAIRS)
    print(merged_dict)