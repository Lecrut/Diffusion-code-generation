def print_first_element(data):
    first = data[:1]
    if first:
        print(first[0])

if __name__ == '__main__':
    sample_list = [10, "hello", 3.14, True]
    print_first_element(sample_list)