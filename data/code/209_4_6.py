def calculate_average(data):
    total = 0
    for item in data:
        if isinstance(item, (int, float)):
            total += item
        else:
            raise TypeError("Input contains non-numeric data")
    if not data:
        return 0
    return total / len(data)
if __name__ == '__main__':
    sample1 = [10, 20, 30, 40]
    sample2 = (5.5, 10.5, 15.5)
    sample3 = [1, 2, "a", 4]
    sample4 = []
    print(f"Average of {sample1}: {calculate_average(sample1)}")
    print(f"Average of {sample2}: {calculate_average(sample2)}")
    try:
        calculate_average(sample3)
    except TypeError as e:
        print(f"Error for {sample3}: {e}")
    print(f"Average of {sample4}: {calculate_average(sample4)}")