def get_first_item(t):
    first, *_ = t
    return first

if __name__ == '__main__':
    sample_tuple = (10, 20, 30)
    result = get_first_item(sample_tuple)
    print(result)