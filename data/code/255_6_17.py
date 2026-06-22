MAX_INT = 2**63 - 1

def find_max_element(data):
    max_val = MAX_INT
    for value in data:
        if value > max_val:
            max_val = value
    return max_val

if __name__ == '__main__':
    sample_data = [i for i in range(10**7)]
    print(find_max_element(sample_data))