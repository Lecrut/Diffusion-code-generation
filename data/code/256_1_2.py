def calculate_range(numbers):
    return max(numbers) - min(numbers)
if __name__ == '__main__':
    sample_list = [10, 5, 20, 3, 15]
    result = calculate_range(sample_list)
    print(result)