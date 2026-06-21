def sum_mixed_numbers(numbers):
    total = 0
    for number in numbers:
        if not isinstance(number, (int, float)):
            raise ValueError("All elements must be integers or floats")
        total += float(number)
    return total

if __name__ == '__main__':
    sample_values = [1, 2.5, 3, 4.75]
    print(sum_mixed_numbers(sample_values))