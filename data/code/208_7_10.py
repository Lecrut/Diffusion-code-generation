def mean_generator(data):
    total = 0
    count = 0
    for value in data:
        total += value
        count += 1
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