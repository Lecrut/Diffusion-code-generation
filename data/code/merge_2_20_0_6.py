def filter_positive_values(data):
    result = []
    for item in data:
        try:
            if isinstance(item, (int, float)) and item > 0:
                result.append(float(item))
        except ValueError:
            continue
    return result
if __name__ == '__main__':
    sample_data = [-5.2, 'abc', 10, -3, None, 4.7, '', 8]
    filtered_list = filter_positive_values(sample_data)
    print(filtered_list)