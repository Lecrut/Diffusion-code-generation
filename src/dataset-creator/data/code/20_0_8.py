def filter_positive_values(data):
    filtered_data = []
    for item in data:
        try:
            num = float(item)
            if num >= 0:
                filtered_data.append(num)
        except (ValueError, TypeError):
            continue
    return filtered_data
if __name__ == '__main__':
    sample_list = [10, -5.2, "abc", 3.4, None, -7, 0, "", 8]
    result = filter_positive_values(sample_list)
    print(result)