class ExtremesCalculator:
    def __init__(self, data):
        self.data = data

    def calculate_difference(self):
        if not self.data:
            raise ValueError("Data cannot be empty.")
        return max(self.data.values()) - min(self.data.values())

if __name__ == '__main__':
    sample_dict_1 = {'a': 10, 'b': 20, 'c': 5}
    calculator_1 = ExtremesCalculator(sample_dict_1)
    result_1 = calculator_1.calculate_difference()
    print(f"Difference in {sample_dict_1}: {result_1}")

    sample_dict_2 = {'x': -3, 'y': 7, 'z': 0}
    calculator_2 = ExtremesCalculator(sample_dict_2)
    result_2 = calculator_2.calculate_difference()
    print(f"Difference in {sample_dict_2}: {result_2}")

    sample_dict_3 = {'m': 100, 'n': -50, 'o': 75}
    calculator_3 = ExtremesCalculator(sample_dict_3)
    result_3 = calculator_3.calculate_difference()
    print(f"Difference in {sample_dict_3}: {result_3}")