FIRST_LAST_LIST = [1, 2, 3, 4, 5]

def print_first_last(lst):
    if lst:
        print(lst[0], lst[-1])

if __name__ == '__main__':
    print_first_last(FIRST_LAST_LIST)