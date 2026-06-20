def starts_with_a_or_b(strings):
    for string in strings:
        if string.startswith('A') or string.startswith('B'):
            return True
    return False

if __name__ == '__main__':
    sample_strings1 = ['Apple', 'Banana', 'Cherry']
    sample_strings2 = ['Durian', 'Elderberry', 'Fig']
    print(f"Sample 1: {starts_with_a_or_b(sample_strings1)}")
    print(f"Sample 2: {starts_with_a_or_b(sample_strings2)}")