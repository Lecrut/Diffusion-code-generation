def filter_odd_numbers(numbers):
    odd_numbers = []
    for num in numbers:
        if num % 2 != 0:
            odd_numbers.append(num)
    return odd_numbers
if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = filter_odd_numbers(sample_data)
    print(result)