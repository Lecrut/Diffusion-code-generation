def validate_input(numbers):
    if not all(isinstance(x, int) for x in numbers):
        raise ValueError("All elements in the tuple must be integers.")
    if len(numbers) == 0:
        raise ValueError("The tuple cannot be empty.")

def find_min_max(numbers):
    validate_input(numbers)
    return min(numbers), max(numbers)

if __name__ == '__main__':
    sample_data1 = (10, 5, 20, 3, 15)
    min1, max1 = find_min_max(sample_data1)
    print(f"Data set 1: {sample_data1}")
    print(f"Minimum: {min1}, Maximum: {max1}")