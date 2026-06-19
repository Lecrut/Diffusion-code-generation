def extract_odd_numbers(numbers):
    odd_numbers = [num for num in numbers if num % 2 != 0]
    return odd_numbers

if __name__ == '__main__':
    sample_list = [10, 23, 45, 68, 79, 82, 91]
    result = extract_odd_numbers(sample_list)
    print(result)