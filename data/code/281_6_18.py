def validate_input(numbers):
    if len(numbers) != 9:
        raise ValueError("Input must contain exactly nine integers.")
    for num in numbers:
        if not isinstance(num, int):
            raise TypeError("All elements must be integers.")

def sum_of_nine_integers(numbers):
    validate_input(numbers)
    return sum(numbers)

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = sum_of_nine_integers(sample_values)
    print(result)