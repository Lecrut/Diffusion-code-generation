def find_highest_value(data):
    if not data:
        raise ValueError("Input dictionary cannot be empty")
    return max(data.values())

if __name__ == '__main__':
    sample_dict1 = {'a': 1, 'b': 5, 'c': 2, 'd': 9, 'e': 3}
    sample_dict2 = {'x': -10, 'y': -5, 'z': -1}
    sample_dict3 = {}

    try:
        result1 = find_highest_value(sample_dict1)
        print(f"Highest value in {sample_dict1}: {result1}")
        result2 = find_highest_value(sample_dict2)
        print(f"Highest value in {sample_dict2}: {result2}")
        find_highest_value(sample_dict3)
    except ValueError as e:
        print(f"Error caught: {e}")