def validate_input(data):
    if not isinstance(data, list) or not all(isinstance(x, int) for x in data):
        raise ValueError("Input must be a list of integers.")

def find_min_max(data):
    validate_input(data)
    if not data:
        return None, None
    return min(data), max(data)

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 8]
    print(find_min_max(sample_list))
    sample_list_empty = []
    print(find_min_max(sample_list_empty))