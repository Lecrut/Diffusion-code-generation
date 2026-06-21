def reverse_range(start, stop):
    return range(start - 1, stop - 1, -1)

if __name__ == '__main__':
    for number in reverse_range(10, 5):
        print(number)