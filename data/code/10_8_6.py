def print_first_element(lst):
    first_element = lst[:1][0]
    print(first_element)

if __name__ == '__main__':
    sample_list = [42, "hello", 3.14, True]
    print_first_element(sample_list)