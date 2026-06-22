def find_minimum(numbers):
    if not numbers:
        raise ValueError("The list cannot be empty")
    return min(numbers)

if __name__ == '__main__':
    sample_numbers = [45, 12, 89, 3, 67, 22]
    try:
        print(find_minimum(sample_numbers))
    except ValueError as e:
        print(e)