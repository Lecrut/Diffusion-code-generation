def get_head(t):
    if len(t) == 0:
        raise IndexError("tuple is empty")
    return t[0]

if __name__ == '__main__':
    sample_tuple = (10, 20, 30, 40)
    result = get_head(sample_tuple)
    print(result)