def print_first_last(items):
    if items:
        print(items[0], items[-1])

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print_first_last(sample_list)