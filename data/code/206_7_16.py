def find_min_ascii(strings):
    if not strings:
        return None
    min_string = min(strings, key=lambda s: sum(ord(c) for c in s))
    return min_string

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry']
    print("Minimum ASCII string:", find_min_ascii(sample_list))