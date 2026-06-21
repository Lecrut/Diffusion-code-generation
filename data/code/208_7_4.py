def mean_generator(data):
    total = 0
    count = 0
    for value in data:
        total += value
        count += 1
        yield (total / count)
if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    mean_gen = mean_generator(sample_data)
    print(next(mean_gen))
    print(next(mean_gen))
    print(next(mean_gen))
    print(next(mean_gen))
    print(next(mean_gen))