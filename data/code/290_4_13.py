class WeightConverter:
    def pounds_to_kilograms(self, weight_pounds):
        if weight_pounds < 0:
            raise ValueError("Weight cannot be negative.")
        return round(weight_pounds * 0.453592, 1)

if __name__ == '__main__':
    converter = WeightConverter()
    sample_weights = [0, 150, -10, 300]
    for weight in sample_weights:
        try:
            result = converter.pounds_to_kilograms(weight)
            print(f"{weight} pounds is {result} kilograms")
        except ValueError as e:
            print(e)