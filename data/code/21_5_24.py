def reverse_range(start, stop):
    current = start
    while current > stop:
        yield current
        current -= 1

if __name__ == '__main__':
    for number in reverse_range(10, 0):
        print(number)