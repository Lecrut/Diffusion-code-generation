UPPER_CASE = str.upper

def map_to_upper_case(strings):
    return list(map(UPPER_CASE, strings))

if __name__ == '__main__':
    sample_strings = ["hello", "world", "this", "is", "a", "test"]
    upper_cased_strings = map_to_upper_case(sample_strings)
    print(upper_cased_strings)