def reverse_range(start, stop):
    for num in range(start, stop - 1, -1):
        yield num

if __name__ == '__main__':
    upper_bound = 25
    lower_bound = 20
    for number in reverse_range(upper_bound, lower_bound):
        print(number)