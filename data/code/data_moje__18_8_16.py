MIDDLE_INDEX_KEY = 'target'
INDEX_MULTIPLIER = 2

def extract_midpoint(data_source):
    if not data_source:
        return None
    mid = len(data_source) // INDEX_MULTIPLIER
    return data_source[mid]

if __name__ == '__main__':
    test_values = [5, 10, 15, 20, 25]
    output = extract_midpoint(test_values)
    print(output)