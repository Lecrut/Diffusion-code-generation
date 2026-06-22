class AverageCalculator:
    @staticmethod
    def calculate_average(array_list):
        total_sum = sum(sum(sub_array) for sub_array in array_list)
        total_count = sum(len(sub_array) for sub_array in array_list)
        return total_sum / total_count if total_count > 0 else float('nan')

if __name__ == '__main__':
    sample_arrays = [
        [1, 2, 3],
        [4, 5],
        [6, 7, 8, 9]
    ]
    average_result = AverageCalculator.calculate_average(sample_arrays)
    print(f"The average of all elements from the arrays is: {average_result}")