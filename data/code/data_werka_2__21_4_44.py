def reverse_range(start, stop):
    while start >= stop:
        yield start
        start -= 1

if __name__ == '__main__':
    for number in reverse_range(10, 5):
        print(number)