def compute_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
if __name__ == '__main__':
    data1 = (10, 20, 30, 40, 50)
    avg1 = compute_average(data1)
    print(f"Average of {list(data1)} is: {avg1}")
    data2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    avg2 = compute_average(data2)
    print(f"Average of {data2} is: {avg2}")
    data3 = (100,)
    avg3 = compute_average(data3)
    print(f"Average of {data3} is: {avg3}")
    data4 = ()
    avg4 = compute_average(data4)
    print(f"Average of {data4} is: {avg4}")