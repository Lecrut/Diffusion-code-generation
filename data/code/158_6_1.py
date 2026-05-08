def filter_even_recursive(data, index, result):
    if index >= len(data):
        if result:
            return result
        return result
    current_element = data[index]
    if current_element % 2 == 0:
        result.append(current_element)
    return filter_even_recursive(data, index + 1, result)
if __name__ == '__main__':
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result_list = []
    filter_even_recursive(input_list, 0, result_list)
    print(result_list)