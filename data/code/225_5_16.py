import statistics

def find_extremes(data_list: list) -> tuple:
    if not data_list:
        return None, None
    minimum = min(data_list)
    maximum = max(data_list)
    return minimum, maximum

if __name__ == '__main__':
    sample_data = {
        'list1': [1, 5, 2, 8, 3],
        'list2': [-10, 0, 5, -5],
        'list3': [42]
    }
    
    for key, data in sample_data.items():
        print(f"List: {data}, Min: {find_extremes(data)}, Max: {find_extremes(data)}")