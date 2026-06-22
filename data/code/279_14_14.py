def cycle_and_print_positives(start=-10, end=10):
    for num in range(start, end + 1):
        if num > 0:
            print(num)

if __name__ == '__main__':
    cycle_and_print_positives()