def flatten_tuple(t):
    return [x for x in t] * 5

if __name__ == '__main__':
    result = flatten_tuple((1, 2, 3))
    print(result)