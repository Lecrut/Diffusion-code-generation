def find_max_value(data):
    if not data:
        raise ValueError("List is empty")
    max_val = data[0]
    for num in data:
        if num > max_val:
            max_val = num
    return max_val

if __name__ == '__main__':
    values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    result = find_max_value(values)
    print(result)