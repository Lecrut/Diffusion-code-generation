def find_max_recursive(data):
    if not data:
        raise ValueError("Empty list provided")
    if len(data) == 1:
        return data[0]
    else:
        first = data[0]
        rest = data[1:]
        max_of_rest = find_max_recursive(rest)
        return max(first, max_of_rest)
if __name__ == '__main__':
    sample_list = [3, 1, 9, 4, 7, 2]
    try:
        maximum = find_max_recursive(sample_list)
        print(maximum)
    except ValueError as e:
        print(e)