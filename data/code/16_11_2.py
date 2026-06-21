def get_first_item(t):
    first, *rest = t
    return first

if __name__ == '__main__':
    result = get_first_item((10, 20, 30))
    print(result)