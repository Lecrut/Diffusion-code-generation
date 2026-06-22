def find_median(data):
    n = len(data)
    if n % 2 == 1:
        return data[n // 2]
    else:
        middle_right_index = n // 2
        middle_left_index = middle_right_index - 1
        return (data[middle_left_index] + data[middle_right_index]) / 2.0

if __name__ == '__main__':
    sample_list = [1, 3, 8, 9, 15]
    print(f"Median of {sample_list}: {find_median(sample_list)}")