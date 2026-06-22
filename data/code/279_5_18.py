def print_positive_numbers(start, end):
    for num in range(start, end + 1):
        if num > 0:
            print(num)

if __name__ == '__main__':
    sample_start = -5
    sample_end = 5
    print("Positive numbers between", sample_start, "and", sample_end, ":")
    print_positive_numbers(sample_start, sample_end)