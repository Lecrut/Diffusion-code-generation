def contains_target(iterable, target):
    if not hasattr(iterable, '__iter__'):
        raise ValueError("First argument must be iterable")
    if not isinstance(target, (int, str)):
        raise ValueError("Second argument must be an integer or string")
    return any(item == target for item in iterable)

if __name__ == '__main__':
    data1 = (1, 5, 2, 8, 3)
    target1 = 8
    result1 = contains_target(data1, target1)
    print(f"Does {target1} exist in {data1}? {result1}")
    
    data2 = ('a', 'b', 'c', 'd')
    target2 = 'z'
    result2 = contains_target(data2, target2)
    print(f"Does {target2} exist in {data2}? {result2}")
    
    data3 = (10, 20, 30)
    target3 = 25
    result3 = contains_target(data3, target3)
    print(f"Does {target3} exist in {data3}? {result3}")
    
    data4 = ('apple', 'banana', 'cherry')
    target4 = 'banana'
    result4 = contains_target(data4, target4)
    print(f"Does {target4} exist in {data4}? {result4}")