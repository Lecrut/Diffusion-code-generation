def is_valid_input(data):
    if not isinstance(data, list):
        raise TypeError("Input must be a list")
    for item in data:
        if not isinstance(item, int):
            raise ValueError("List elements must be integers")

def find_minimum(data):
    is_valid_input(data)
    if not data:
        return None
    minimum = data[0]
    for item in data[1:]:
        if item < minimum:
            minimum = item
    return minimum

if __name__ == '__main__':
    sample_list = [45, 12, 89, 3, 56, 7]
    result = find_minimum(sample_list)
    print(result)