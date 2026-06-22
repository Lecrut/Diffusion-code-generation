def head(t: tuple) -> object:
    return t[0]

if __name__ == '__main__':
    sample_tuple = (10, 20, 30)
    result = head(sample_tuple)
    print(result)