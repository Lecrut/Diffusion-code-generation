def starts_with_a_or_b(strings):
    for s in strings:
        if s.startswith('A') or s.startswith('B'):
            return True
    return False

if __name__ == '__main__':
    sample_strings = ['apple', 'banana', 'cherry']
    result = starts_with_a_or_b(sample_strings)
    print(f"Result: {result}")