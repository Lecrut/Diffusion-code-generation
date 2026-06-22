class AverageCalculator:
    @staticmethod
    def calculate_average(arrays):
        total_sum = sum(sum(array) for array in arrays)
        total_count = sum(len(array) for array in arrays)
        if total_count > 0:
            return total_sum / total_count
        else:
            return None

if __name__ == '__main__':
    sample_arrays = [
        [1, 2, 3],
        [4, 5],
        [6, 7, 8, 9]
    ]
    average = AverageCalculator.calculate_average(sample_arrays)
    print(f"The average of all elements from the arrays is: {average}")