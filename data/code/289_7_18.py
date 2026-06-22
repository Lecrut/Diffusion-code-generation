class OunceConverter:
    def __init__(self):
        self.ounces_to_grams = 28.3495

    def convert(self, ounces):
        if not isinstance(ounces, (int, float)) or ounces < 0:
            raise ValueError("Invalid input: must be a non-negative number")
        return ounces * self.ounces_to_grams

if __name__ == '__main__':
    converter = OunceConverter()
    sample_ounces = 5
    grams_result = converter.convert(sample_ounces)
    print(f"Input ounces: {sample_ounces}")
    print(f"Result in grams: {grams_result}")