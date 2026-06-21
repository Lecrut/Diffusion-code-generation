def calculate_average(data):
    if not hasattr(data, '__iter__'):
        raise ValueError("Input is not iterable")
    
    try:
        total = sum(1 for _ in data)
        if total == 0:
            return 0
        
        count = sum(1 for _ in data)
        average = sum(data) / count
        return average
    
    except TypeError:
        raise ValueError("Elements of the input are not numbers")

if __name__ == '__main__':
    sample1 = [10, 20, 30, 40, 50]
    sample2 = [5.5, 6.5, 7.5]
    sample3 = []
    
    print(f"Average of sample1: {calculate_average(sample1)}")
    print(f"Average of sample2: {calculate_average(sample2)}")
    try:
        print(f"Average of sample3: {calculate_average(sample3)}")
    except ValueError as e:
        print(e)