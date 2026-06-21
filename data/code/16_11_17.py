def extract_first(t):
    first, *_ = t
    return first

if __name__ == '__main__':
    sample_tuple = (10, 20, 30)
    result = extract_first(sample_tuple)
    print(result)