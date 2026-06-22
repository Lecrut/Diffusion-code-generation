def reverse_range(start, stop):
    if start <= stop:
        return
    while start > stop:
        yield start
        start -= 1

if __name__ == '__main__':
    for number in reverse_range(25, 20):
        print(number)