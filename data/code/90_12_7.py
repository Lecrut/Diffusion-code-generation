def any_starts_with_ab(strings):
    for s in strings:
        if s.startswith('A') or s.startswith('B'):
            return True
    return False

if __name__ == '__main__':
    test_strings1 = ['Apple', 'Banana', 'Cherry']
    test_strings2 = ['Grape', 'Kiwi', 'Lemon']
    print(f"Test 1: {any_starts_with_ab(test_strings1)}")
    print(f"Test 2: {any_starts_with_ab(test_strings2)}")