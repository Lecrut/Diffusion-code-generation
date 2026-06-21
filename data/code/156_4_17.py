def compute_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    data1 = (10, 20, 30, 40, 50)
    avg1 = compute_average(data1)
    print(f"Average of {data1}: {avg1}")
    
    data2 = [5, 15, 25, 35]
    avg2 = compute_average(data2)
    print(f"Average of {data2}: {avg2}")
    
    data3 = []
    avg3 = compute_average(data3)
    print(f"Average of {data3}: {avg3}")