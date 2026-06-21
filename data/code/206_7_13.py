def find_min_ascii(data):
    if not data:
        return None
    return min(data, key=lambda x: sum(ord(c) for c in x))

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry']
    print("Minimum value based on ASCII:", find_min_ascii(sample_list))