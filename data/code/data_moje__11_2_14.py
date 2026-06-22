def get_last_element(lst):
    result = lst[-1:]
    return result[0]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = get_last_element(sample_list)
    print(result)