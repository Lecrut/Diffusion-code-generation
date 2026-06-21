def find_middle(data):
    n = len(data)
    if n == 0:
        raise ValueError("Empty list")
    return data[n // 2]

if __name__ == '__main__':
    sample_list = [1, 5, 2, 8, 3]
    middle_value = find_middle(sample_list)
    print(middle_value)