class WeightConverter:
    def __init__(self):
        self.conversion_factor = 0.453592

    def pounds_to_kilograms(self, pounds):
        return pounds * self.conversion_factor

if __name__ == '__main__':
    converter = WeightConverter()
    sample_pounds = 10.0
    kilograms_result = converter.pounds_to_kilograms(sample_pounds)
    print(f"{sample_pounds} lbs is {kilograms_result} kg")