def filter_positive_values(data_stream):
    return (value for value in data_stream if value >= 0)
if __name__ == '__main__':
    large_data = [10, -5, 3, -20, 7, -89]
    filtered_result = list(filter_positive_values(large_data))
    print(filtered_result)