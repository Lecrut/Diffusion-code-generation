def calculate_lengths(a, b):
    lengths = {'length1': a, 'length2': b}
    difference = abs(a - b)
    ratio = max(a, b) / min(a, b) if min(a, b) != 0 else float('inf')
    lengths['difference'] = difference
    lengths['ratio'] = ratio
    return lengths

if __name__ == '__main__':
    result = calculate_lengths(10, 5)
    print(result)