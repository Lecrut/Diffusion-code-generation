def find_max_in_strings(string_list):
    if not string_list:
        return None
    max_value = int(string_list[0])
    for value in string_list:
        try:
            num = int(value)
            if num > max_value:
                max_value = num
        except ValueError:
            continue
    return max_value

if __name__ == '__main__':
    data1 = ["10", "5", "20", "8", "30"]
    print("Max of data1:", find_max_in_strings(data1))
    data2 = ["-5", "-1", "-10", "-2"]
    print("Max of data2:", find_max_in_strings(data2))
    data3 = ["42"]
    print("Max of data3:", find_max_in_strings(data3))
    data4 = []
    print("Max of data4:", find_max_in_strings(data4))