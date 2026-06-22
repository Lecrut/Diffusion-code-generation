def reverse_range(start, stop):
    decrement = 1
    current = start - decrement
    while current >= stop:
        yield current
        current -= decrement

if __name__ == '__main__':
    for number in reverse_range(25, 20):
        print(number)