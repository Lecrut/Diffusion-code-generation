def map_to_upper(strings):
    return list(map(lambda s: s.upper(), strings))

if __name__ == '__main__':
    sample_strings = ["hello", "world", "python"]
    upper_strings = map_to_upper(sample_strings)
    print(upper_strings)