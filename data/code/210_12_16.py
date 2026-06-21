MIN_VALUE = float('-inf')
MAX_VALUE = float('inf')

def determine_range(data):
    if not data:
        return MIN_VALUE, MAX_VALUE
    minimum = maximum = data[0]
    for x in data[1:]:
        if x < minimum:
            minimum = x
        elif x > maximum:
            maximum = x
    return minimum, maximum

if __name__ == '__main__':
    sample_data1 = [10, 5, 20, 15, 8]
    result1 = determine_range(sample_data1)
    print(f"Data: {sample_data1}, Range: {result1}")
    
    sample_data2 = [3.14, -1.5, 9.8, 0.5]
    result2 = determine_range(sample_data2)
    print(f"Data: {sample_data2}, Range: {result2}")