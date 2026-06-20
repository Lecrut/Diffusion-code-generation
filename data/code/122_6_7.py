def running_average(sequence):
    n = 0
    mean = 0
    for value in sequence:
        n += 1
        delta = value - mean
        mean += delta / n
    return mean

if __name__ == '__main__':
    sample_sequence = [1, 2, 3, 4, 5]
    print(running_average(sample_sequence))