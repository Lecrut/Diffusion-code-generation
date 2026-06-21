def filter_elements(predicate, elements):
    return [item for item in elements if not predicate(item)]

if __name__ == '__main__':
    sample_values = [10, 23, 45, 68, 90]
    condition = lambda value: value > 50
    filtered_result = filter_elements(condition, sample_values)
    print(filtered_result)