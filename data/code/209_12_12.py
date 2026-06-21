def calculate_average(data):
    if not hasattr(data, '__iter__') or isinstance(data, str):
        raise ValueError("Input must be an iterable of numbers")
    return sum(data) / len(data)

if __name__ == '__main__':
    sample1 = [10, 20, 30, 40, 50]
    sample2 = [5.5, 6.5, 7.5]
    sample3 = []
    
    try:
        average1 = calculate_average(sample1)
        print(f"Average of sample1: {average1}")
        
        average2 = calculate_average(sample2)
        print(f"Average of sample2: {average2}")
        
        average3 = calculate_average(sample3)
        print(f"Average of sample3: {average3}")
    except ValueError as e:
        print(e)