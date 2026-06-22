def reverse_range(start, stop):
    upper_bound = start - 1
    while upper_bound >= stop:
        yield upper_bound
        upper_bound -= 1

if __name__ == '__main__':
    for number in reverse_range(30, 25):
        print(number)