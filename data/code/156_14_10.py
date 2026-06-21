import math

def calculate_average(numbers):
    if not numbers:
        return 0
    return math.fsum(numbers) / len(numbers)

if __name__ == '__main__':
    data1 = [1, 2, 3, 4, 5]
    avg1 = calculate_average(data1)
    print(f"Average of {data1}: {avg1}")
    
    data2 = [10, 20, 30, 40, 50, 60]
    avg2 = calculate_average(data2)
    print(f"Average of {data2}: {avg2}")
    
    data3 = []
    avg3 = calculate_average(data3)
    print(f"Average of {data3}: {avg3}")
    
    data4 = [1.5, 2.5, 3.5]
    avg4 = calculate_average(data4)
    print(f"Average of {data4}: {avg4}")