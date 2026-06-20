def has_negative(data):
    return any(x < 0 for x in data)

if __name__ == '__main__':
    test_values = [-1, 2, 3, -4, 5]
    print(has_negative(test_values))