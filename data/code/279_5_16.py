def print_positive_numbers(start, end):
    if start > end:
        return
    for num in range(start, end + 1):
        if num > 0:
            print(num)

if __name__ == '__main__':
    print("Printing positive numbers from -5 to 5:")
    print_positive_numbers(-5, 5)