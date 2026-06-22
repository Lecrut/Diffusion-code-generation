AVG_INIT_COUNT = 0
AVG_INIT_TOTAL = 0

def average_generator(values):
    count = AVG_INIT_COUNT
    total = AVG_INIT_TOTAL
    for value in values:
        count += 1
        total += value
        yield (total / count)

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    avg_gen = average_generator(sample_values)
    print(next(avg_gen))
    print(next(avg_gen))
    print(next(avg_gen))
    print(next(avg_gen))
    print(next(avg_gen))