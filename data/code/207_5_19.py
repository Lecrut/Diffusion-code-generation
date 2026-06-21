def find_max_in_strings(str_list):
    if not all((isinstance(item, str) and item.isdigit() for item in str_list)):
        raise ValueError('All elements in the list must be strings representing digits.')
    return max((int(item) for item in str_list))
if __name__ == '__main__':
    data1 = ['10', '5', '20', '8', '30']
    print(find_max_in_strings(data1))
    data2 = ['-5', '-1', '-10', '-2']
    print(find_max_in_strings(data2))
    data3 = ['42']
    print(find_max_in_strings(data3))
    data4 = []
    try:
        print(find_max_in_strings(data4))
    except ValueError as e:
        print(e)
    data5 = ['10', '5', '20a', '8', '30']
    try:
        print(find_max_in_strings(data5))
    except ValueError as e:
        print(e)