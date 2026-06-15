def contains_target(iterable, target):
    return any(item == target for item in iterable)
if __name__ == '__main__':
    data1 = [1, 5, 2, 8, 3]
    target1 = 8
    result1 = contains_target(data1, target1)
    print(f"List: {data1}, Target: {target1}, Contains: {result1}")
    data2 = [10, 20, 30, 40]
    target2 = 5
    result2 = contains_target(data2, target2)
    print(f"List: {data2}, Target: {target2}, Contains: {result2}")
    data3 = ['a', 'b', 'c']
    target3 = 'd'
    result3 = contains_target(data3, target3)
    print(f"List: {data3}, Target: {target3}, Contains: {result3}")
    data4 = [1, 2, 3]
    target4 = 2
    result4 = contains_target(data4, target4)
    print(f"List: {data4}, Target: {target4}, Contains: {result4}")