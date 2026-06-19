def compare_lengths(length1, length2):
    return (min(length1, length2), max(length1, length2))

if __name__ == '__main__':
    sample_values = {
        'length_a': 30,
        'length_b': 45
    }
    
    result = compare_lengths(sample_values['length_a'], sample_values['length_b'])
    print(result)