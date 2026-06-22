def reverse_range(start, stop):
    return (num for num in range(start - 1, stop - 1, -1))

if __name__ == '__main__':
    for number in reverse_range(25, 20):
        print(number)