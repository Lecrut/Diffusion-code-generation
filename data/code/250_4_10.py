def average_generator(values):
    total = 0
    count = 0
    for value in values:
        count += 1
        total += value
        yield total / count

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    avg_gen = average_generator(sample_values)
    print(next(avg_gen))
    print(next(avg_gen))
    print(next(avg_gen))
    print(next(avg_gen))
    print(next(avg_gen))