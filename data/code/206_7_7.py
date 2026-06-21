def min_ascii_value(strings):
    return min(strings, key=lambda s: sum(ord(c) for c in s))

if __name__ == '__main__':
    sample_values = ["apple", "banana", "cherry"]
    print(min_ascii_value(sample_values))