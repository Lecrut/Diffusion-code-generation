def get_head_of_tuple(t):
    if not t:
        return None
    return t[0]

if __name__ == '__main__':
    sample_tuple = (10, 20, 30)
    result = get_head_of_tuple(sample_tuple)
    print(result)