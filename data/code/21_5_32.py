def reverse_range(start, stop):
    for num in range(stop - 1, start - 1, -1):
        yield num

if __name__ == '__main__':
    sample_start = 0
    sample_stop = 10
    for number in reverse_range(sample_start, sample_stop):
        print(number)