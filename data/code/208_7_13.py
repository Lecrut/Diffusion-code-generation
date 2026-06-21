def mean_generator(data):
    count = 0
    total = 0
    for value in data:
        count += 1
        total += value
        yield total / count

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    mean_gen = mean_generator(sample_data)
    print(next(mean_gen))
    print(next(mean_gen))
    print(next(mean_gen))
    print(next(mean_gen))
    print(next(mean_gen))

    sample_data_2 = [1.5, 2.5, 3.5, 4.5]
    mean_gen_2 = mean_generator(sample_data_2)
    print(next(mean_gen_2))
    print(next(mean_gen_2))
    print(next(mean_gen_2))
    print(next(mean_gen_2))

    empty_data = []
    try:
        next(mean_generator(empty_data))
    except StopIteration:
        print("Empty data, no mean")