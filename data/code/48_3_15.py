def find_largest_value(d):
    return max(d.values())

if __name__ == '__main__':
    data = {'a': 10, 'b': 25, 'c': 5}
    print(find_largest_value(data))