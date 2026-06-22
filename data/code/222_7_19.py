MIN_VALUE = float('inf')

def find_minimum(data):
    if not data:
        return None
    current_min = MIN_VALUE
    for item in data:
        if item < current_min:
            current_min = item
    return current_min

if __name__ == '__main__':
    large_list = [5, 12, 3, 8, 1, 15, -4, 9, 0, 22]
    print(find_minimum(large_list))