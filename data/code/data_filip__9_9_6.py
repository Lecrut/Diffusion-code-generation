def strip_tuple_strings(strings_tuple):
    result = tuple(s.strip() for s in strings_tuple)
    return result

if __name__ == '__main__':
    sample_data = ("  hello  ", "world  ", "  foo bar  ")
    cleaned_data = strip_tuple_strings(sample_data)
    print(cleaned_data)