def get_middle_value(data_list):
    n = len(data_list)
    if n == 0:
        return None
    mid_index = n // 2
    if n % 2 != 0:
        return data_list[mid_index]
    else:
        return (data_list[mid_index - 1] + data_list[mid_index]) / 2

if __name__ == '__main__':
    sample_list = [100, 200, 300]
    print(f"Middle value of {sample_list}: {get_middle_value(sample_list)}")