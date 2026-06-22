def find_middle_element(data):
    count = len(data)
    if count < 1:
        raise ValueError("Input list cannot be empty")
    midpoint_index = (count - 1) // 2
    return data[midpoint_index]

if __name__ == '__main__':
    odd_sequence = [100, 200, 300, 400, 500]
    even_sequence = [10, 20, 30, 40]
    odd_result = find_middle_element(odd_sequence)
    even_result = find_middle_element(even_sequence)
    print(odd_result)
    print(even_result)