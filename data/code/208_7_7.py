def mean_generator(data):
    count = 0
    total = 0
    for value in data:
        count += 1
        total += value
        yield (total / count)
if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    mean_gen = mean_generator(sample_data)
    print(next(mean_gen))
    print(next(mean_gen))
    print(next(mean_gen))
    print(next(mean_gen))
    print(next(mean_gen))