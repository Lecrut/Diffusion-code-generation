def any_starts_with_ab(strings):
    return any(s.startswith('A') or s.startswith('B') for s in strings)

if __name__ == '__main__':
    sample_strings = ['Apple', 'Banana', 'Cherry', 'Date']
    result = any_starts_with_ab(sample_strings)
    print(f"Result: {result}")