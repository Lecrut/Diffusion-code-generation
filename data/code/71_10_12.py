def find_middle_element(data):
    n = len(data)
    if n % 2 == 1:
        return data[n // 2]
    else:
        left_mid = data[(n - 1) // 2]
        right_mid = data[n // 2]
        return (left_mid + right_mid) / 2

if __name__ == '__main__':
    sample_list = [1, 3, 5, 7, 9, 11]
    print(find_middle_element(sample_list))