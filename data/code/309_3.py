def sum_generator(iterable):
    return sum(x for x in iterable)
if __name__ == '__main__':
    data1 = (1, 2, 3, 4, 5)
    result1 = sum_generator(data1)
    print(f"Sum of {data1}: {result1}")
    data2 = [10, 20, 30]
    result2 = sum_generator(data2)
    print(f"Sum of {data2}: {result2}")
    data3 = (1.5, 2.5, 3.0)
    result3 = sum_generator(data3)
    print(f"Sum of {data3}: {result3}")
    data4 = []
    result4 = sum_generator(data4)
    print(f"Sum of {data4}: {result4}")