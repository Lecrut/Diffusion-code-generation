def compare_adjacent_strings(strings):
    LATER = lambda s1, s2: s2 if s2 > s1 else s1
    return [LATER(s, t) for s, t in zip(strings, strings[1:])]

if __name__ == '__main__':
    sample_values = ["apple", "banana", "cherry", "date"]
    result = compare_adjacent_strings(sample_values)
    print(result)