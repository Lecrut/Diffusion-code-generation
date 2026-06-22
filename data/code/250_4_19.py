def average_generator(values):
    count = 0
    total = 0
    for value in values:
        count += 1
        total += value
        yield (total / count)

if __name__ == '__main__':
    sample_values = [3, 6, 9, 12, 15]
    avg_gen = average_generator(sample_values)
    print(next(avg_gen))
    print(next(avg_gen))
    print(next(avg_gen))
    print(next(avg_gen))
    print(next(avg_gen))