def find_odd_numbers(numbers):
    return [num for num in numbers if num & 1]

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(find_odd_numbers(sample_values))