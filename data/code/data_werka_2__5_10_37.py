def length_difference(a, b):
    return max(0, abs(a - b))

if __name__ == '__main__':
    sample_lengths = {'length1': 20, 'length2': 5}
    result = length_difference(sample_lengths['length1'], sample_lengths['length2'])
    print(result)