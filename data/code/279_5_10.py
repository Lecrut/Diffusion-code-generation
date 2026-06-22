def print_positive_numbers(start, end):
    for i in range(start, end + 1):
        if i > 0:
            print(i)

if __name__ == '__main__':
    start = -5
    end = 5
    print("Positive numbers between", start, "and", end)
    print_positive_numbers(start, end)