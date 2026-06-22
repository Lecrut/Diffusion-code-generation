CHAR_ORDER = {
    'ASCENDING': 1,
    'DESCENDING': -1
}

def compare_adjacent_chars(a, b):
    if ord(a) < ord(b):
        return CHAR_ORDER['ASCENDING']
    elif ord(a) > ord(b):
        return CHAR_ORDER['DESCENDING']
    else:
        return 0

def classify_adjacent_pairs(input_string):
    results = []
    for i in range(len(input_string) - 1):
        result = compare_adjacent_chars(input_string[i], input_string[i+1])
        if result == CHAR_ORDER['ASCENDING']:
            results.append('ascending')
        elif result == CHAR_ORDER['DESCENDING']:
            results.append('descending')
        else:
            results.append('equal')
    return results

if __name__ == '__main__':
    sample_input = 'abcde'
    output = classify_adjacent_pairs(sample_input)
    print(output)