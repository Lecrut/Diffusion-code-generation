def get_element_safe(t, index):
    if 0 <= index < len(t):
        return t[index]
    return None

if __name__ == '__main__':
    sample_tuple = (10, 20, 30, 40, 50)
    print(get_element_safe(sample_tuple, 2))
    print(get_element_safe(sample_tuple, 10))
    print(get_element_safe(sample_tuple, 0))
    print(get_element_safe(sample_tuple, -1))