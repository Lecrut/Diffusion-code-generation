def is_even(number):
    return isinstance(number, int) and number % 2 == 0

def filter_even_numbers(numbers):
    even_numbers = []
    for num in numbers:
        if is_even(num):
            even_numbers.append(num)
    return even_numbers

if __name__ == '__main__':
    sample_values = [10, 23, 456, -89, "test", None, 78]
    result = filter_even_numbers(sample_values)
    print(result)