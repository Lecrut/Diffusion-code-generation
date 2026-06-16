def number_cycler(start, end):
    current = start
    while current <= end:
        yield current
        current += 1
if __name__ == '__main__':
    start_val = 5
    end_val = 15
    cycler = number_cycler(start_val, end_val)
    for num in cycler:
        print(num)