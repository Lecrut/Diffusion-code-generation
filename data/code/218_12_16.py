def find_smallest(input_dict, default=None):
    try:
        if not input_dict:
            return default
        return min(input_dict.values())
    except Exception as e:
        raise ValueError(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    sample_dict = {'a': 10, 'b': -3, 'c': 8}
    result = find_smallest(sample_dict)
    print(result)