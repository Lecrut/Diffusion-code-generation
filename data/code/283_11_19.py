def ensure_strings(lst):
    return [str(item) for item in lst]

if __name__ == '__main__':
    sample_list = [1, '2', 3.0, None]
    result = ensure_strings(sample_list)
    print(result)