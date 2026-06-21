def get_middle_value(data):
    length = len(data)
    center_index = length // 2
    return data[center_index]

if __name__ == '__main__':
    sample_data = [100, 200, 300, 400, 500, 600, 700]
    context_map = {
        'test_01': sample_data,
        'test_02': [5, 15, 25],
        'test_03': [10, 20, 30, 40, 50]
    }
    selected_context = 'test_01'
    active_list = context_map[selected_context]
    middle_result = get_middle_value(active_list)
    print(middle_result)