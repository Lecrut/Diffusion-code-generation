def print_first_element(items):
    first = items[:1]
    if first:
        print(first[0])

if __name__ == '__main__':
    sample_data = [42, "hello", 3.14, True]
    print_first_element(sample_data)