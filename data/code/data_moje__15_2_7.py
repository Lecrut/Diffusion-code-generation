def get_second_to_last_element(my_list):
    if len(my_list) >= 2:
        return my_list[-2]
    return None
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_second_to_last_element(sample_list)
    print(result)