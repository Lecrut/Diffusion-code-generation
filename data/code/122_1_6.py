def calculate_average(numbers):
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    data1 = [3, 6, 9, 12, 15]
    data2 = [2, 4, 8, 10]
    
    avg1 = calculate_average(data1)
    avg2 = calculate_average(data2)

    print(f"Average of {data1}: {avg1}")
    print(f"Average of {data2}: {avg2}")