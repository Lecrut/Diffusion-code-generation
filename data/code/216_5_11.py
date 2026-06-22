def is_valid_list(data):
    if not isinstance(data, list) or len(data) < 1:
        raise ValueError("Input must be a non-empty list")

def get_middle_value(data):
    n = len(data)
    is_valid_list(data)
    if n % 2 == 0:
        return (data[n // 2 - 1] + data[n // 2]) / 2
    else:
        return data[n // 2]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Middle value for even length list:", get_middle_value(sample_list))
    sample_list_odd = [10, 20, 30, 40, 50]
    print("Middle value for odd length list:", get_middle_value(sample_list_odd))