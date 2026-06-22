def find_absolute_minimum(numbers):
    if not numbers:
        return None
    if any(not isinstance(num, complex) for num in numbers):
        return None
    return min(numbers, key=lambda x: abs(x))

if __name__ == '__main__':
    sample_numbers = [3+4j, 1-2j, -5+6j, 7+8j]
    result = find_absolute_minimum(sample_numbers)
    print(result)