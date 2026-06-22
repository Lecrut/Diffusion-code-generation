def print_positive_numbers(start, end):
    for i in range(start, end + 1):
        if i > 0:
            print(i)

if __name__ == '__main__':
    print_positive_numbers(-5, 5)