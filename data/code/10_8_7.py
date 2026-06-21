def extract_first_element(lst):
    first = lst[:1]
    print(first)
    return first

if __name__ == '__main__':
    sample_list = [42, "hello", 3.14, True, None]
    extract_first_element(sample_list)