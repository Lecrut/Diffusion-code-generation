def map_strings_to_uppercase(strings):
    return list(map(lambda s: s.upper(), strings))

if __name__ == '__main__':
    sample_values = ["hello", "world", "python", "programming"]
    print(map_strings_to_uppercase(sample_values))