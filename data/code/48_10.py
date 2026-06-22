def find_largest(values):
    largest = values[0]
    for value in values[1:]:
        if value > largest:
            largest = value
    return largest

if __name__ == '__main__':
    data = [12, 5, 34, 7, 89, 23, 45, 67, 1, 99]
    result = find_largest(data)
    print(result)