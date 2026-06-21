def find_highest_value(data):
    if not data:
        raise ValueError("Input dictionary cannot be empty")
    return max(data.values())

if __name__ == '__main__':
    sample_dict = {'a': 10, 'b': 20, 'c': 5, 'd': 30}
    try:
        result = find_highest_value(sample_dict)
        print(f"Highest value in {sample_dict}: {result}")
    except ValueError as e:
        print(f"Error caught: {e}")