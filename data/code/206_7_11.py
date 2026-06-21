def find_min_ascii_value(data):
    if not data:
        return None
    current_min = data[0]
    for element in data[1:]:
        if ord(element) < ord(current_min):
            current_min = element
    return current_min

if __name__ == '__main__':
    sample_list = ['a', 'z', 'c', 'm']
    print("Minimum ASCII value:", find_min_ascii_value(sample_list))