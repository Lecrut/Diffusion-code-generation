import statistics

def find_extremes(data_list: list) -> tuple:
    if not data_list:
        return None, None
    minimum = min(data_list)
    maximum = max(data_list)
    return minimum, maximum

if __name__ == '__main__':
    sample_data1 = [1, 5, 2, 8, 3]
    print(f"List: {sample_data1}, Min: {find_extremes(sample_data1)[0]}, Max: {find_extremes(sample_data1)[1]}")
    
    sample_data2 = [-10, 0, 5, -5]
    print(f"List: {sample_data2}, Min: {find_extremes(sample_data2)[0]}, Max: {find_extremes(sample_data2)[1]}")
    
    sample_data3 = [42]
    print(f"List: {sample_data3}, Min: {find_extremes(sample_data3)[0]}, Max: {find_extremes(sample_data3)[1]}")