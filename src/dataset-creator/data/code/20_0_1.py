def filter_positive_values(data):
    result = []
    for item in data:
        try:
            if isinstance(item, (int, float)) and item > 0:
                result.append(item)
        except TypeError:
            continue
    return result
if __name__ == '__main__':
    sample_data = [1, -5, "a", None, 3.5, -2.7, True]
    filtered_list = filter_positive_values(sample_data)
    print(filtered_list)