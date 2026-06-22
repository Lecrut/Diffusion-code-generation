MIN_VALUE = float('-inf')
MAX_VALUE = float('inf')

def get_min_max(data_tuple):
    if not data_tuple:
        return None, None
    
    minimum = MAX_VALUE
    maximum = MIN_VALUE
    
    for item in data_tuple:
        if item < minimum:
            minimum = item
        if item > maximum:
            maximum = item
            
    return minimum, maximum

if __name__ == '__main__':
    sample_data1 = (10, 5, 20, 8, 15)
    min1, max1 = get_min_max(sample_data1)
    print(f"Data: {sample_data1}, Minimum: {min1}, Maximum: {max1}")