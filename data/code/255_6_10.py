def find_max_in_memory(data):
    max_val = data[0]
    for value in data:
        if value > max_val:
            max_val = value
    return max_val

if __name__ == '__main__':
    sample_data = [i for i in range(10**7)]
    print(find_max_in_memory(sample_data))