def get_first_item(t):
    first, *rest = t
    return first

if __name__ == '__main__':
    sample_tuple = (42, 'hello', 3.14)
    result = get_first_item(sample_tuple)
    print(result)