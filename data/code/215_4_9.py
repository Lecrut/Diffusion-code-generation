def find_largest_number(values):
    if not values:
        raise ValueError("Input dictionary cannot be empty")
    return max(values.values())

if __name__ == '__main__':
    sample_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
    try:
        print(f"Largest number: {find_largest_number(sample_dict)}")
    except ValueError as e:
        print(e)