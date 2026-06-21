def check_first_and_last(lst):
    return lst[0], lst[-1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    first, last = check_first_and_last(sample_list)
    print(first, last)