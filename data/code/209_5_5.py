def running_average_generator(samples):
    if not samples:
        return
    current_sum = 0
    count = 0
    for sample in samples:
        current_sum += sample
        count += 1
        yield current_sum / count
if __name__ == '__main__':
    data_stream = [10, 20, 30, 40, 50, 60]
    average_gen = running_average_generator(data_stream)
    print("Running Averages:")
    for avg in average_gen:
        print(avg)