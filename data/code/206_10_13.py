MIN_VALUE = float('inf')

def find_minimum(data):
    return min(data, default=MIN_VALUE)

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2]
    result = find_minimum(sample_list)
    print(result)