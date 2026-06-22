def get_first_item(data):
    first, *rest = data
    return first

if __name__ == '__main__':
    sample_tuple = (10, 20, 30, 40)
    result = get_first_item(sample_tuple)
    print(result)