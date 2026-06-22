MIDDLE_INDEX = 1

def get_middle_value(data_list):
    n = len(data_list)
    if n == 0:
        return None
    else:
        middle_index = (n - 1) // 2
        if (n - 1) % 2 != 0:
            return data_list[middle_index + MIDDLE_INDEX]
        else:
            return data_list[middle_index]

if __name__ == '__main__':
    sample_list_odd = [1, 2, 3, 4, 5]
    sample_list_even = [10, 20, 30, 40]
    sample_list_single = [99]
    sample_list_empty = []
    print(f"Middle value of {sample_list_odd}: {get_middle_value(sample_list_odd)}")
    print(f"Middle value of {sample_list_even}: {get_middle_value(sample_list_even)}")
    print(f"Middle value of {sample_list_single}: {get_middle_value(sample_list_single)}")
    print(f"Middle value of {sample_list_empty}: {get_middle_value(sample_list_empty)}")