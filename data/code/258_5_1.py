def running_sum_count_generator(data):
    running_sum = 0
    count = 0
    yield None, None
    for i, (value1, value2) in enumerate(data):
        running_sum += value1 + value2
        count += 1
        if count == 1:
            yield running_sum, count
        elif count == 2:
            yield running_sum, count
if __name__ == '__main__':
    sample_data = [(10, 5), (20, 8), (30, 12), (40, 15)]
    generator = running_sum_count_generator(sample_data)
    print("Running Sum and Count for First Two Elements:")
    for item in generator:
        print(item)