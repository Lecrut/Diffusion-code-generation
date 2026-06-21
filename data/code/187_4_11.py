def is_valid_list(data):
    if not isinstance(data, list) or not all(isinstance(x, (int, float)) for x in data):
        raise ValueError("Input must be a non-empty list of numbers")

def find_largest(data):
    is_valid_list(data)
    return max(data)

if __name__ == '__main__':
    list1 = [3, 1, 4, 1, 5, 9, 2]
    print(find_largest(list1))
    list2 = [-10, -5, -20, -1]
    print(find_largest(list2))