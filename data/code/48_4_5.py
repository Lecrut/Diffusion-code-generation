def find_largest_value():
    data = [10, 25, 3, 42, 15, 6, 99, 55, 33, 7]
    largest = None
    for value in data:
        if largest is None or value > largest:
            largest = value
            yield largest
    return largest

def get_final_maximum():
    generator = find_largest_value()
    result = None
    for value in generator:
        result = value
    return result

if __name__ == '__main__':
    print(get_final_maximum())