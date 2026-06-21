MIN_VALUE = float('inf')

def get_minimum(items):
    return min(items, default=MIN_VALUE)

if __name__ == '__main__':
    sample_list = [15, 3, 8, 22, 1]
    minimum_value = get_minimum(sample_list)
    print(minimum_value)