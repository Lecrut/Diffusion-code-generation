def find_max_element(data):
    max_val = data[0]
    for value in data:
        if value > max_val:
            max_val = value
    return max_val

if __name__ == '__main__':
    sample_data = [i for i in range(10**7)]
    result = find_max_element(sample_data)
    print(result)