def print_first_last(items):
    if items:
        first = items[0]
        last = items[-1]
        print(first, last)
    else:
        print("List is empty")

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print_first_last(sample_list)