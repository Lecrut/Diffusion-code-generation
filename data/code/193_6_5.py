def is_valid_number(value):
    return isinstance(value, (int, float))

def sum_mixed_numbers(numbers):
    total = 0
    for number in numbers:
        if not is_valid_number(number):
            raise ValueError("All elements in the list must be int or float")
        total += number
    return total

if __name__ == '__main__':
    sample_values = [1, 2.5, 3, 4.75]
    result = sum_mixed_numbers(sample_values)
    print(result)