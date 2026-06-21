def find_middle(data):
    n = len(data)
    if n % 2 == 1:
        return data[n // 2]
    else:
        return (data[n // 2 - 1] + data[n // 2]) / 2

if __name__ == '__main__':
    sample_list = [3, 7, 5, 9, 11, 13]
    middle_value = find_middle(sample_list)
    print(middle_value)