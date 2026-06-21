def collect_odd_numbers(numbers):
    odd_numbers = []
    for number in numbers:
        if number % 2 != 0:
            odd_numbers.append(number)
    return odd_numbers
if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = collect_odd_numbers(sample_data)
    print(result)