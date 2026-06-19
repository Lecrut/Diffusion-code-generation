def access_and_verify_element(data_list, index):
    try:
        assert 0 <= index < len(data_list), 'Index out of bounds'
        element = data_list[index]
        assert element == data_list[index], 'Element verification failed'
        return element
    except AssertionError as e:
        print(e)
        return None
if __name__ == '__main__':
    sample_data = [5, 15, 25, 35, 45, 55]
    target_position = 3
    result = access_and_verify_element(sample_data, target_position)
    print(result)