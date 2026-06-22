MAX_VALUE = float('-inf')

def find_max_element(data):
    max_val = MAX_VALUE
    for value in data:
        if value > max_val:
            max_val = value
    return max_val

if __name__ == '__main__':
    sample_data = [i for i in range(10**6)]
    print(find_max_element(sample_data))