def contains_target(iterable, target):
    return any(item == target for item in iterable)
if __name__ == '__main__':
    data1 = [1, 5, 2, 8, 3]
    target1 = 8
    result1 = contains_target(data1, target1)
    print(f"Does {target1} exist in {data1}? {result1}")
    data2 = [10, 20, 30, 40]
    target2 = 5
    result2 = contains_target(data2, target2)
    print(f"Does {target2} exist in {data2}? {result2}")
    data3 = ['a', 'b', 'c']
    target3 = 'd'
    result3 = contains_target(data3, target3)
    print(f"Does {target3} exist in {data3}? {result3}")
    data4 = [1, 2, 3]
    target4 = 2
    result4 = contains_target(data4, target4)
    print(f"Does {target4} exist in {data4}? {result4}")