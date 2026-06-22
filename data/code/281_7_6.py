def sum_ten_numbers(**kwargs):
    total = 0.0
    for value in kwargs.values():
        total += value
    return total

if __name__ == '__main__':
    sample_values = {'a': 1.5, 'b': 2.75, 'c': 3.0, 'd': -4.2, 'e': 100.1}
    result = sum_ten_numbers(**sample_values)
    print(result)