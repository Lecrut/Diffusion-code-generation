def calculate_average(data):
    total = 0
    count = 0
    for item in data:
        if isinstance(item, (int, float)):
            total += item
            count += 1
        else:
            raise TypeError("Input contains non-numeric data")
    if count == 0:
        return 0
    return total / count
if __name__ == '__main__':
    data1 = (10, 20, 30, 40)
    data2 = [5.5, 10.5, 15.5]
    data3 = (1, 2, "three", 4)
    data4 = []
    try:
        avg1 = calculate_average(data1)
        print(f"Average of {data1}: {avg1}")
        avg2 = calculate_average(data2)
        print(f"Average of {data2}: {avg2}")
        print("Attempting to calculate average for data3...")
        avg3 = calculate_average(data3)
        print(f"Average of {data3}: {avg3}")
    except TypeError as e:
        print(f"Caught expected error for data3: {e}")
    try:
        avg4 = calculate_average(data4)
        print(f"Average of {data4}: {avg4}")
    except TypeError as e:
        print(f"Caught expected error for data4: {e}")