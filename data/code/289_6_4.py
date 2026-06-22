class WeightConverter:
    KILOGRAMS_PER_GRAM = 1 / 1000

    @staticmethod
    def grams_to_kilograms(grams):
        return grams * WeightConverter.KILOGRAMS_PER_GRAM

if __name__ == '__main__':
    converter = WeightConverter()
    print(f"2500 grams is {converter.grams_to_kilograms(2500)} kilograms")
    print(f"1500000 grams is {converter.grams_to_kilograms(1500000)} kilograms")