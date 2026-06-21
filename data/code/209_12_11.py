def calculate_average(data):
    if not hasattr(data, '__iter__'):
        raise TypeError("Input must be iterable")
    
    total = sum(data)
    count = len(data)
    
    if count == 0:
        return 0
    
    average = total / count
    return average

if __name__ == '__main__':
    sample1 = [10, 20, 30, 40, 50]
    sample2 = [5.5, 6.5, 7.5]
    sample3 = []
    
    avg1 = calculate_average(sample1)
    print(f"Average of sample1: {avg1}")
    
    avg2 = calculate_average(sample2)
    print(f"Average of sample2: {avg2}")
    
    try:
        avg3 = calculate_average(sample3)
        print(f"Average of sample3: {avg3}")
    except TypeError as e:
        print(e)