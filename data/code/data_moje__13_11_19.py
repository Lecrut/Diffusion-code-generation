def safe_tuple_get(t, index):
    if 0 <= index < len(t):
        return t[index]
    return None

if __name__ == '__main__':
    sample_tuple = (10, 20, 30, 40, 50)
    print(safe_tuple_get(sample_tuple, 2))
    print(safe_tuple_get(sample_tuple, 5))
    print(safe_tuple_get(sample_tuple, -1))
    print(safe_tuple_get(sample_tuple, 0))