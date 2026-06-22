class AverageCalculator:
    def __init__(self, data):
        self.data = data

    def calculate_average(self):
        total_sum = sum(sum(subset) for subset in self.data)
        total_count = sum(len(subset) for subset in self.data)
        if total_count > 0:
            return total_sum / total_count
        else:
            return None

if __name__ == '__main__':
    calculator = AverageCalculator([
        [1, 2, 3],
        [4, 5],
        [6, 7, 8, 9]
    ])
    average = calculator.calculate_average()
    print(f"The average of all elements from the subsets is: {average}")