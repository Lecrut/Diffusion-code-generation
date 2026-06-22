def get_last_element(collection):
    return collection[-1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_tuple = ('a', 'b', 'c')
    sample_string = "optimization"
    result_list = get_last_element(sample_list)
    result_tuple = get_last_element(sample_tuple)
    result_string = get_last_element(sample_string)
    print(result_list)
    print(result_tuple)
    print(result_string)