def print_first_last(lst):
    if lst:
        print(lst[0], lst[-1])

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print_first_last(sample_list)