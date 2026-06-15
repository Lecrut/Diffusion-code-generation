def calculate_running_average(data_list, new_figure):
    if not data_list:
        return new_figure
    data_list.append(new_figure)
    running_sum = sum(data_list)
    count = len(data_list)
    return running_sum / count
if __name__ == '__main__':
    data = []
    print(f"Initial state: {data}")
    new_val1 = 10
    avg1 = calculate_running_average(data, new_val1)
    print(f"After adding {new_val1}: {data}, Running Average: {avg1}")
    new_val2 = 20
    avg2 = calculate_running_average(data, new_val2)
    print(f"After adding {new_val2}: {data}, Running Average: {avg2}")
    new_val3 = 30
    avg3 = calculate_running_average(data, new_val3)
    print(f"After adding {new_val3}: {data}, Running Average: {avg3}")