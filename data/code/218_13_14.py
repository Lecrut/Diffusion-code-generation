def find_min(numbers):
    if not numbers:
        raise ValueError("The list of numbers cannot be empty")
    return min(numbers)

if __name__ == '__main__':
    sample_values = [34, 56, 23, 89, 1]
    try:
        print(find_min(sample_values))
    except ValueError as e:
        print(e)