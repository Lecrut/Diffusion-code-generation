def find_min_value(numbers):
    if not numbers:
        return None
    min_value = numbers[0]
    for number in numbers[1:]:
        if number < min_value:
            min_value = number
    return min_value

if __name__ == '__main__':
    sample_values = [
        [5, 2, 8, 1, 9],
        [-10, 0, 5, -3],
        [42],
        []
    ]
    for values in sample_values:
        print(f"Smallest in {values}: {find_min_value(values)}")