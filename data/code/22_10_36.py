ODD_THRESHOLD = 1

def filter_odd_numbers(numbers):
    def is_odd(number):
        return number % 2 != 0

    odd_numbers = []
    for num in numbers:
        if is_odd(num) and num > ODD_THRESHOLD:
            odd_numbers.append(num)
    return odd_numbers

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    odd_numbers = filter_odd_numbers(sample_values)
    print(odd_numbers)