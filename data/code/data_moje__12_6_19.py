def get_center_element(data):
    length = len(data)
    if length == 0:
        return None
    return data[length // 2]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_tuple = ('a', 'b', 'c', 'd', 'e', 'f')
    print(get_center_element(sample_list))
    print(get_center_element(sample_tuple))
    print(get_center_element([]))
    print(get_center_element((42,)))