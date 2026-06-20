def print_first_last(items):
    if not items:
        print("List is empty")
    else:
        first = items[0]
        last = items[-1]
        print(first, last)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print_first_last(sample_list)