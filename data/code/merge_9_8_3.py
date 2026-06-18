def calculate_running_average(data_list, new_figure):
    if not data_list:
        return new_figure
    current_sum = sum(data_list) + new_figure
    count = len(data_list) + 1
    return current_sum / count
if __name__ == '__main__':
    data = []
    running_averages = []
    new_figure_1 = 10
    data.append(new_figure_1)
    avg_1 = calculate_running_average(data, new_figure_1)
    running_averages.append(avg_1)
    print(f"Data: {data}, Running Average after adding {new_figure_1}: {avg_1}")
    new_figure_2 = 20
    data.append(new_figure_2)
    avg_2 = calculate_running_average(data, new_figure_2)
    running_averages.append(avg_2)
    print(f"Data: {data}, Running Average after adding {new_figure_2}: {avg_2}")
    new_figure_3 = 30
    data.append(new_figure_3)
    avg_3 = calculate_running_average(data, new_figure_3)
    running_averages.append(avg_3)
    print(f"Data: {data}, Running Average after adding {new_figure_3}: {avg_3}")
    print(f"\nFinal Data: {data}")
    print(f"All Running Averages: {running_averages}")