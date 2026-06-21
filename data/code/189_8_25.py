def custom_filter(elements, condition):
    filtered_elements = [element for element in elements if not condition(element)]
    return filtered_elements

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    condition_function = lambda x: x > 25
    result = custom_filter(sample_values, condition_function)
    print(result)