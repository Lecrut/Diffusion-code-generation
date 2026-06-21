class AverageCalculator:
    @staticmethod
    def calculate_average(data):
        if not isinstance(data, list):
            return None
        if not data:
            return 0
        try:
            total = sum(data)
            average = total / len(data)
            return average
        except TypeError:
            return None

if __name__ == '__main__':
    calculator = AverageCalculator()
    sample_lists = [
        [1, 2, 3, 4, 5],
        [],
        ["a", "b", "c"],
        [10, 20, "error"]
    ]
    for lst in sample_lists:
        print(f"Average of {lst}: {calculator.calculate_average(lst)}")