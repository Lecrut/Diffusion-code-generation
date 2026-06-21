def reverse_range(start, stop):
    step = start - 1
    while step >= stop:
        yield step
        step -= 1

if __name__ == '__main__':
    for number in reverse_range(20, 15):
        print(number)