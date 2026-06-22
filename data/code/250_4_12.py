def average_generator(values):
    total = 0
    count = 0
    for value in values:
        total += value
        count += 1
        yield total / count

if __name__ == '__main__':
    sample_values = [5, 15, 25, 35, 45]
    avg_gen = average_generator(sample_values)
    print(next(avg_gen))
    print(next(avg_gen))
    print(next(avg_gen))
    print(next(avg_gen))
    print(next(avg_gen))