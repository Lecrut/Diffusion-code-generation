def get_head(t):
    if not t:
        return None
    return t[0]

if __name__ == '__main__':
    sample_tuple = (42, 3.14, "hello")
    empty_tuple = ()
    result1 = get_head(sample_tuple)
    result2 = get_head(empty_tuple)
    print(result1)
    print(result2)