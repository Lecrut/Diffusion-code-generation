GROUPED = {}

def categorize_strings(strings):
    for string in strings:
        first_char = string[0]
        if first_char not in GROUPED:
            GROUPED[first_char] = []
        GROUPED[first_char].append(string)
    
    return dict(sorted(GROUPED.items()))

if __name__ == '__main__':
    sample_values = ["apple", "banana", "avocado", "cherry", "blueberry", "apricot"]
    result = categorize_strings(sample_values)
    print(result)