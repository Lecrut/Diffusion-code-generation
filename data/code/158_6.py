def filter_even_recursive(data, index=0):
    if index >= len(data):
        return []
    current_element = data[index]
    if current_element % 2 == 0:
        result = [current_element]
    else:
        result = []
    remaining_result = filter_even_recursive(data, index + 1)
    if result:
        return result + remaining_result
    else:
        return remaining_result
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = filter_even_recursive(sample_list)
    print(result)