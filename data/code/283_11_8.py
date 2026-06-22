def ensure_strings(lst):
    return [str(item) for item in lst]

if __name__ == '__main__':
    sample_list = ['apple', 42, 'banana', True]
    result = ensure_strings(sample_list)
    print(result)