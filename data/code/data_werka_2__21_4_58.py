def reverse_range(start, stop):
    current = start - 1
    while current >= stop:
        yield current
        current -= 1

if __name__ == '__main__':
    lower_bound = 30
    upper_bound = 25
    for number in reverse_range(lower_bound, upper_bound):
        print(number)