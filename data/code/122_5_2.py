def running_average_generator(data_stream):
    total = 0
    count = 0
    for number in data_stream:
        total += number
        count += 1
        yield total / count
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    average_gen = running_average_generator(sample_data)
    print("Running averages:")
    for avg in average_gen:
        print(avg)