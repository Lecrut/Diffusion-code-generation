def get_max_element(sorted_list):
    return sorted_list[-1]

if __name__ == '__main__':
    data = [7, 3, 5, 9, 2]
    max_value = get_max_element(data)
    print(max_value)