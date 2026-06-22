def find_max_custom():
    data = [3.14, 1.59, 2.65, 3.58, 9.79, 3.23, 8.46]
    max_val = data[0]
    for val in data:
        if val > max_val:
            max_val = val
    return max_val

if __name__ == '__main__':
    result = find_max_custom()
    print(result)