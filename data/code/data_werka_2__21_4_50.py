def reverse_range(start, stop):
    START = start
    STOP = stop

    while START >= STOP:
        yield START
        START -= 1

if __name__ == '__main__':
    for number in reverse_range(15, 10):
        print(number)