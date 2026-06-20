def running_average(sequence):
    count = 0
    mean = 0.0
    for value in sequence:
        count += 1
        delta = value - mean
        mean += delta / count
        yield mean

if __name__ == '__main__':
    sample_sequence = [1, 2, 3, 4, 5]
    averages = list(running_average(sample_sequence))
    print(averages)