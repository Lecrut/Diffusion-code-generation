def find_max_element(data):
    max_val = data[0]
    for value in data:
        if value > max_val:
            max_val = value
    return max_val

if __name__ == '__main__':
    sample_data = [i * i for i in range(1, 10**6)]
    print(find_max_element(sample_data))