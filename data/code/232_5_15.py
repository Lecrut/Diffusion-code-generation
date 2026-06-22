def growing_number_sequence():
    i = 0
    while i <= 99:
        yield i
        i += 1

if __name__ == '__main__':
    sequence = growing_number_sequence()
    for number in sequence:
        print(number)