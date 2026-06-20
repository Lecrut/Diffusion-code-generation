def calculate_average(numbers):
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    data1 = [10, 20, 30, 40, 50]
    data2 = [100, 200, 300]
    try:
        avg1 = calculate_average(data1)
        print(f"Average of {data1}: {avg1}")
        avg2 = calculate_average(data2)
        print(f"Average of {data2}: {avg2}")
    except ValueError as e:
        print(f"Error: {e}")