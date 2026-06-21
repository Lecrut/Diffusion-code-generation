def calculate_mean(data):
    total = 0
    count = 0
    for value in data:
        total += value
        count += 1
    if count == 0:
        return None
    return total / count

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    mean_value = calculate_mean(sample_data)
    print(mean_value)
    sample_data_2 = [1.5, 2.5, 3.5, 4.5]
    mean_value_2 = calculate_mean(sample_data_2)
    print(mean_value_2)
    empty_data = []
    mean_value_empty = calculate_mean(empty_data)
    print(mean_value_empty)