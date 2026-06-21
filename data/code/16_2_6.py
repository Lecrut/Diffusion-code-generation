def get_head(t):
    if not t:
        raise IndexError("cannot get head of an empty tuple")
    return t[0]

if __name__ == '__main__':
    sample_tuple = (42, 17, 99)
    result = get_head(sample_tuple)
    print(result)