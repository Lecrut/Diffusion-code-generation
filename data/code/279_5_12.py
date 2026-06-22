def print_positive_numbers(start, end):
    if start > end:
        return
    for i in range(start, end + 1):
        if i > 0:
            print(i)

if __name__ == '__main__':
    print("Printing positive numbers from -5 to 5:")
    print_positive_numbers(-5, 5)