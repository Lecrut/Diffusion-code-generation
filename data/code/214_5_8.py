import math
def find_absolute_minimum(iterable):
    try:
        iterator = iter(iterable)
        first_value = next(iterator)
    except StopIteration:
        raise ValueError("Iterable is empty")
    minimum = first_value
    for value in iterator:
        if value < minimum:
            minimum = value
    return minimum
if __name__ == '__main__':
    data1 = [5, -2, 8, -10, 3]
    print(f"Data: {data1}, Minimum: {find_absolute_minimum(data1)}")
    data2 = [10, 5, 20, 1]
    print(f"Data: {data2}, Minimum: {find_absolute_minimum(data2)}")
    data3 = [-5, -1, -10, -3]
    print(f"Data: {data3}, Minimum: {find_absolute_minimum(data3)}")
    data4 = [42]
    print(f"Data: {data4}, Minimum: {find_absolute_minimum(data4)}")
    def number_generator():
        yield 100
        yield 50
        yield -20
        yield 75
    data5 = number_generator()
    print(f"Data (Generator): Iterating through values, Minimum: {find_absolute_minimum(data5)}")
    try:
        data6 = []
        find_absolute_minimum(data6)
    except ValueError as e:
        print(f"Data: {data6}, Error: {e}")