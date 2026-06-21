def find_min_ascii_value(data):
    if not data:
        return None
    current_min = min(data)
    return current_min

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry']
    print("Minimum ASCII value:", find_min_ascii_value(sample_list))