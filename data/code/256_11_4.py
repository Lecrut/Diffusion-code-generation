import math
def calculate_figure_range(numbers):
    if not numbers:
        return 0
    return max(numbers) - min(numbers)
if __name__ == '__main__':
    sample_list = [15, 3, 8, 22, 1]
    result = calculate_figure_range(sample_list)
    print(result)