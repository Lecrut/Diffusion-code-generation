def filter_positive_values(data):
    result = []
    for item in data:
        try:
            num = float(item)
            if num >= 0:
                result.append(num)
        except (ValueError, TypeError):
            continue
    return result
if __name__ == '__main__':
    sample_data = [10, -5.2, "abc", None, 3.14, "", -7]
    filtered_result = filter_positive_values(sample_data)
    print(filtered_result)