def ensure_strings(lst):
    return [str(item) for item in lst]

if __name__ == '__main__':
    sample_list = ['apple', 42, 3.14, True, None]
    converted_list = ensure_strings(sample_list)
    print(converted_list)