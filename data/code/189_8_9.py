def filter_elements(elements, condition):
    return [item for item in elements if not condition(item)]

if __name__ == '__main__':
    sample_data = [10, 23, 45, 68, 90]
    criteria = lambda value: value < 50
    filtered_result = filter_elements(sample_data, criteria)
    print(filtered_result)