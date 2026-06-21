def validate_input(numbers):
    if not all(isinstance(x, int) for x in numbers):
        raise ValueError("All elements must be integers.")

def reverse_list(numbers):
    return list(reversed(numbers))

if __name__ == '__main__':
    sample_input = [1, 5, 3, 9, 2]
    try:
        validate_input(sample_input)
        reversed_list = reverse_list(sample_input)
        print(reversed_list)
    except ValueError as e:
        print(f"Error: {e}")