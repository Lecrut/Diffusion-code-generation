def find_max_in_dict_values(data):
    if not data:
        raise ValueError("Input dictionary cannot be empty")
    return max(data.values())

if __name__ == '__main__':
    sample_dict = {'a': 10, 'b': 20, 'c': 5}
    try:
        result = find_max_in_dict_values(sample_dict)
        print(f"Max value in {sample_dict}: {result}")
    except ValueError as e:
        print(f"Error caught: {e}")