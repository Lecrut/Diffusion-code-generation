class WeightConverter:
    def pounds_to_kilograms(self, pounds: float) -> float:
        return pounds * 0.453592

if __name__ == '__main__':
    converter = WeightConverter()
    sample_pounds = 100.0
    kilograms_result = converter.pounds_to_kilograms(sample_pounds)
    print(f"{sample_pounds} lbs is {kilograms_result} kg")