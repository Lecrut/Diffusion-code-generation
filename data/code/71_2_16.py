def find_middle_value(data):
    n = len(data)
    if n == 0:
        return None
    middle_index = n // 2
    return data[middle_index]

if __name__ == '__main__':
    sample_list_odd = [1, 5, 2, 8, 3]
    sample_list_even = [10, 20, 30, 40]
    print(f"Middle value of {sample_list_odd} is {find_middle_value(sample_list_odd)}")
    print(f"Middle value of {sample_list_even} is {find_middle_value(sample_list_even)}")