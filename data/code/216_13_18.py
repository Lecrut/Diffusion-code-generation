def find_middle_value(data):
    n = len(data)
    if n == 0:
        return None
    mid_index = n // 2
    if n % 2 == 1:
        return data[mid_index]
    else:
        return (data[mid_index - 1] + data[mid_index]) / 2

if __name__ == '__main__':
    sample_data = [45, 60, 75, 90, 105]
    print(f"Middle value of {sample_data}: {find_middle_value(sample_data)}")