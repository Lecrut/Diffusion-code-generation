def number_cycler(start, end):
    current = start
    while current <= end:
        yield current
        current += 1
if __name__ == '__main__':
    for num in number_cycler(5, 15):
        print(num)