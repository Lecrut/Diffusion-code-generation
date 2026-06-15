def calculate_running_average(data_list, new_figure):
    if not data_list:
        return new_figure
    data_list.append(new_figure)
    running_sum = sum(data_list)
    count = len(data_list)
    return running_sum / count
if __name__ == '__main__':
    data = []
    def update_average(current_data, new_value):
        return calculate_running_average(current_data, new_value)
    print(f"Initial data: {data}")
    new_figure1 = 10
    avg1 = update_average(data, new_figure1)
    print(f"After adding {new_figure1}: Data={data}, Average={avg1:.2f}")
    new_figure2 = 20
    avg2 = update_average(data, new_figure2)
    print(f"After adding {new_figure2}: Data={data}, Average={avg2:.2f}")
    new_figure3 = 30
    avg3 = update_average(data, new_figure3)
    print(f"After adding {new_figure3}: Data={data}, Average={avg3:.2f}")
    new_figure4 = 5
    avg4 = update_average(data, new_figure4)
    print(f"After adding {new_figure4}: Data={data}, Average={avg4:.2f}")