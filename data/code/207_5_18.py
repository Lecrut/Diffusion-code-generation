def find_max_string_numbers(str_list):
    return max(int(num) for num in str_list)

if __name__ == '__main__':
    data1 = ['10', '5', '20', '8', '30']
    print("Max of data1:", find_max_string_numbers(data1))
    data2 = ['-5', '-1', '-10', '-2']
    print("Max of data2:", find_max_string_numbers(data2))
    data3 = ['42']
    print("Max of data3:", find_max_string_numbers(data3))
    data4 = []
    try:
        print("Max of data4:", find_max_string_numbers(data4))
    except ValueError as e:
        print(e)