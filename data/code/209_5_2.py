def running_average_generator(data_stream):
    total = 0
    count = 0
    for sample in data_stream:
        total += sample
        count += 1
        yield total / count
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50, 60, 70]
    running_avg = running_average_generator(sample_data)
    print("Running Averages:")
    for avg in running_avg:
        print(avg)