def calculate_length(data):
    return len(data)

def fetch_middle_element(sequence):
    if not sequence:
        return None
    length = calculate_length(sequence)
    midpoint_index = length // 2
    return sequence[midpoint_index]

if __name__ == '__main__':
    test_values = [7, 14, 21, 28, 35, 42, 49, 56]
    middle_result = fetch_middle_element(test_values)
    print(middle_result)