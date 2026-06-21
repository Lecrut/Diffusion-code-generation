def calculate_mean(data):
    if not data:
        return 0
    total = sum(data)
    count = len(data)
    average = total / count
    return average

if __name__ == '__main__':
    sample_data1 = [2, 4, 6, 8, 10]
    avg1 = calculate_mean(sample_data1)
    print(f"Average of {sample_data1}: {avg1}")

    sample_data2 = (3, 5, 7, 9, 11, 13)
    avg2 = calculate_mean(sample_data2)
    print(f"Average of {sample_data2}: {avg2}")