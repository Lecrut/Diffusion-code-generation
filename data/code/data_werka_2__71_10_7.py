def get_middle_element(data):
    if not isinstance(data, (list, tuple)):
        raise ValueError("Input must be a list or tuple")
    if len(data) == 0:
        raise ValueError("Input sequence must not be empty")
    length = len(data)
    half = length // 2
    if length % 2 == 1:
        return data[half]
    left_slice = data[half - 1:half]
    right_slice = data[half:half + 1]
    return (left_slice[0] + right_slice[0]) / 2.0

if __name__ == '__main__':
    odd_list = [10, 20, 30, 40, 50]
    even_list = [10, 20, 30, 40]
    print(get_middle_element(odd_list))
    print(get_middle_element(even_list))