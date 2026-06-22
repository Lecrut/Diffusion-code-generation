def calculate_length_properties(length1, length2):
    lengths = {'length1': length1, 'length2': length2}
    difference = abs(length1 - length2)
    if length1 > length2:
        ratio = length1 / length2
    else:
        ratio = length2 / length1
    lengths['difference'] = difference
    lengths['ratio'] = ratio
    return lengths

if __name__ == '__main__':
    result = calculate_length_properties(10, 5)
    print(result)