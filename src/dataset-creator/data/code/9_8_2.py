def calculate_running_average(data_list, new_figure):
    if not data_list:
        return new_figure
    data_list.append(new_figure)
    running_sum = sum(data_list)
    count = len(data_list)
    return running_sum / count
if __name__ == '__main__':
    data = []
    def update_and_calculate(data, new_figure):
        result = calculate_running_average(data, new_figure)
        print(f"New figure added: {new_figure}")
        print(f"Current data list: {data}")
        print(f"Running average: {result:.2f}\n")
        return data
    update_and_calculate(data, 10)
    update_and_calculate(data, 20)
    update_and_calculate(data, 30)