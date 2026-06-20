def starts_with_a_or_b(strings):
    for s in strings:
        if s.startswith('A') or s.startswith('B'):
            return True
    return False
if __name__ == '__main__':
    sample_strings1 = ['Apple', 'Banana', 'Cherry']
    sample_strings2 = ['Grape', 'Kiwi', 'Lemon']
    print(f'Sample 1: {starts_with_a_or_b(sample_strings1)}')
    print(f'Sample 2: {starts_with_a_or_b(sample_strings2)}')