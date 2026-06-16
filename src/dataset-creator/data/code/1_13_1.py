def check_criteria(data_list):
    return any(item > 10 for item in data_list)
if __name__ == '__main__':
    sample_data = [5, 8, 3, 20, 7]
    result = check_criteria(sample_data)
    print(result if isinstance(result, bool) else "Invalid output type")