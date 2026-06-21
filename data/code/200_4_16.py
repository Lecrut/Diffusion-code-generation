def multiply_first_elements(data):
    product = 1
    for item in data:
        first_element = item[0]
        product *= ord(first_element)
    return product

if __name__ == '__main__':
    sample_data = [("apple", "banana"), ("cherry", "date"), ("elderberry", "fig")]
    result = multiply_first_elements(sample_data)
    print(result)