def calculate_difference(numbers):
    return max(numbers) - min(numbers)

if __name__ == '__main__':
    sample_list = [10, 3, 5, 8, 2]
    result = calculate_difference(sample_list)
    print(result)