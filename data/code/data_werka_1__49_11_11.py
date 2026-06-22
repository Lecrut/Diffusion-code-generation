def calculate_lengths(a, b):
    lengths = {'length_a': a, 'length_b': b}
    if a > b:
        lengths['difference'] = a - b
        lengths['ratio'] = a / b
    else:
        lengths['difference'] = b - a
        lengths['ratio'] = b / a
    return lengths

if __name__ == '__main__':
    result = calculate_lengths(10, 5)
    print(result)