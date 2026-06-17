def print_indices_with_while(iterable):
    index = 0
    while index < len(iterable):
        print(index)
        index += 1
if __name__ == '__main__':
    sample_data = (10, 20, 30, 40, 50)
    print_indices_with_while(sample_data)