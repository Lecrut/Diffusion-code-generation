def calculate_average(data):
    total = 0
    count = 0
    for item in data:
        if isinstance(item, (int, float)):
            total += item
            count += 1
        else:
            raise TypeError("Input contains non-numeric data.")
    if count == 0:
        return 0
    return total / count
if __name__ == '__main__':
    data1 = (10, 20, 30, 40)
    data2 = [5.5, 10.5, 15.5]
    data3 = (1, 2, "three", 4)
    data4 = []
    data5 = (10, "error", 30)
    print(f"Average of {data1}: {calculate_average(data1)}")
    print(f"Average of {data2}: {calculate_average(data2)}")
    try:
        calculate_average(data3)
    except TypeError as e:
        print(f"Error for {data3}: {e}")
    print(f"Average of {data4}: {calculate_average(data4)}")
    try:
        calculate_average(data5)
    except TypeError as e:
        print(f"Error for {data5}: {e}")