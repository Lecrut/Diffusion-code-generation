def find_middle_value(data):
    n = len(data)
    if n == 0:
        return None
    elif n % 2 != 0:
        return data[n // 2]
    else:
        mid1 = data[n // 2 - 1]
        mid2 = data[n // 2]
        return (mid1 + mid2) / 2
if __name__ == '__main__':
    sample_list_odd = [1, 5, 3, 7, 9]
    sample_list_even = [10, 20, 30, 40]
    sample_list_single = [42]
    sample_list_empty = []
    print(f"Middle value of {sample_list_odd}: {find_middle_value(sample_list_odd)}")
    print(f"Middle value of {sample_list_even}: {find_middle_value(sample_list_even)}")
    print(f"Middle value of {sample_list_single}: {find_middle_value(sample_list_single)}")
    print(f"Middle value of {sample_list_empty}: {find_middle_value(sample_list_empty)}")