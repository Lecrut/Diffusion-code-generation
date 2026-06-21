def calculate_mean(data_generator):
    count = 0
    total_sum = 0
    for value in data_generator:
        count += 1
        total_sum += value
    if count == 0:
        return None
    return total_sum / count
if __name__ == '__main__':
    sample_data_1 = (x for x in range(1, 51))
    mean_value_1 = calculate_mean(sample_data_1)
    print(mean_value_1)
    sample_data_2 = (x * 0.5 for x in range(1, 51))
    mean_value_2 = calculate_mean(sample_data_2)
    print(mean_value_2)
    empty_generator = iter(())
    mean_empty = calculate_mean(empty_generator)
    print(mean_empty)