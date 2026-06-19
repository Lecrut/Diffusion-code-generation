def retrieve_second_value(elements):
    second_index = 1
    return elements[second_index]

if __name__ == '__main__':
    demonstration_list = [42, 84, 168, 336, 672]
    result = retrieve_second_value(demonstration_list)
    print(result)