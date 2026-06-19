def filter_odd_numbers(numbers):
    odd_numbers = []
    for number in numbers:
        if number % 2 != 0:
            odd_numbers.append(number)
    return odd_numbers

if __name__ == '__main__':
    sample_values = [10, 21, 34, 45, 56, 67]
    result = filter_odd_numbers(sample_values)
    print(result)