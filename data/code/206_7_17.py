def find_min_ascii_value(data):
    if not data:
        return None
    current_min = min(data, key=lambda x: ord(x[0]))
    return current_min

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry']
    print("Minimum value based on ASCII:", find_min_ascii_value(sample_list))