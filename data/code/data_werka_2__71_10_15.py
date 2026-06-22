def get_middle_value(data):
    if not data:
        raise ValueError("Sequence must not be empty")
    length = len(data)
    center = length // 2
    if length % 2 == 1:
        return data[center]
    left_val = data[center - 1]
    right_val = data[center]
    return (left_val + right_val) / 2

if __name__ == '__main__':
    odd_data = [10, 20, 30, 40, 50]
    even_data = [10, 20, 30, 40]
    odd_result = get_middle_value(odd_data)
    even_result = get_middle_value(even_data)
    print(odd_result)
    print(even_result)