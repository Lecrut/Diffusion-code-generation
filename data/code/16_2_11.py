def get_head(t):
    return t[0] if t else None

if __name__ == '__main__':
    sample_tuple = (10, 20, 30)
    result = get_head(sample_tuple)
    print(result)