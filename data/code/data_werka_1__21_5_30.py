def reverse_range(start, stop):
    for num in range(stop - 1, start - 1, -1):
        yield num

if __name__ == '__main__':
    start = 0
    stop = 10
    for number in reverse_range(start, stop):
        print(number)