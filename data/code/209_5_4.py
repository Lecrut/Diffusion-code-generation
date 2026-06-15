def running_average_generator(data_stream):
    total = 0
    count = 0
    for sample in data_stream:
        total += sample
        count += 1
        yield total / count
if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    average_gen = running_average_generator(sample_data)
    print("Running Averages:")
    for avg in average_gen:
        print(avg)