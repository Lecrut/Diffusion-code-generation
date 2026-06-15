def calculate_figure_range(numbers):
    if not numbers:
        return 0
    return max(numbers) - min(numbers)
if __name__ == '__main__':
    sample_list = [15, 8, 22, 3, 45, 1]
    result = calculate_figure_range(sample_list)
    print(result)