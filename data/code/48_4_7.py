def max_data_point():
    numbers = [10, 50, 3, 95, 22, 88, 7, 41]
    max_val = numbers[0]
    for val in numbers:
        if val > max_val:
            max_val = val
    yield max_val

if __name__ == '__main__':
    for result in max_data_point():
        print(result)