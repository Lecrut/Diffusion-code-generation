def ensure_strings(lst):
    return [str(item) for item in lst]

if __name__ == '__main__':
    sample_list = ['apple', 2, 'banana', 3.14]
    result = ensure_strings(sample_list)
    print(result)