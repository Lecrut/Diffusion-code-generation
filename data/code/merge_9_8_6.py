def calculate_running_average(data_list, new_figure):
    if not data_list:
        return new_figure
    current_sum = sum(data_list) + new_figure
    count = len(data_list) + 1
    return current_sum / count
if __name__ == '__main__':
    data = []
    running_averages = []
    new_figures = [10, 20, 30, 40, 50]
    for figure in new_figures:
        data.append(figure)
        if data:
            current_sum = sum(data)
            count = len(data)
            running_average = current_sum / count
            running_averages.append(running_average)
        else:
            running_averages.append(0.0)
    print(f"Data added: {data}")
    print(f"Running averages: {running_averages}")