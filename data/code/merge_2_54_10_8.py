def find_middle_position(data):
    if not data:
        return None
    length = len(data)
    if length % 2 == 1:
        middle_index = (length - 1) // 2
        return {
            'index': middle_index,
            'value': data[middle_index],
            'is_even_length': False
        }
    else:
        left_middle = (length - 1) // 2
        right_middle = length // 2
        return {
            'left_index': left_middle,
            'right_index': right_middle,
            'values': [data[left_middle], data[right_middle]],
            'is_even_length': True
        }
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = find_middle_position(sample_list)
    if isinstance(result, dict):
        print(f"Middle position found at index: {result['index']}")
        print(f"Value: {result['value']}")
        is_even_length = 'Yes' if result.get('is_even_length', False) else 'No'
        print(f"List length parity ({len(sample_list)}): {is_even_length}")
    elif isinstance(result, list):
        left_idx = result[0]
        right_idx = result[1]
        print(f"Middle positions found at indices: {left_idx} and {right_idx}")
        print(f"Values: {[result[i] for i in range(2)]}")
    else:
        print("No middle position exists.")