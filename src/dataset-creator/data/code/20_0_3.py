def filter_positive_values(data):
    result = []
    for item in data:
        try:
            if float(item) >= 0:
                result.append(float(item))
        except (ValueError, TypeError):
            continue
    return result
if __name__ == '__main__':
    sample_data = [10, -5, 'a', None, 3.5, '-2', True, False]
    filtered_list = filter_positive_values(sample_data)
    print(filtered_list)