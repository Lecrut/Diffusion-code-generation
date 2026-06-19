def compare_adjacent_numbers(data):
    n = len(data)
    for i in range(n - 1):
        if not (isinstance(data[i], (int, float)) and isinstance(data[i+1], (int, float))):
            raise TypeError(f"Non-numeric adjacent elements found: {data[i]} and {data[i+1]}")
        if data[i] > data[i+1]:
            return False
    return True

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [1.0, 2.5, 3.1, 4.8, 5.0]
    list3 = ['a', 2, 3, 'b']
    list4 = [5, 4, 3, 2, 1]
    list5 = [10]
    list6 = []
    
    try:
        print(compare_adjacent_numbers(list1))
    except TypeError as e:
        print(e)
    
    try:
        print(compare_adjacent_numbers(list2))
    except TypeError as e:
        print(e)
    
    try:
        print(compare_adjacent_numbers(list3))
    except TypeError as e:
        print(e)
    
    try:
        print(compare_adjacent_numbers(list4))
    except TypeError as e:
        print(e)
    
    try:
        print(compare_adjacent_numbers(list5))
    except TypeError as e:
        print(e)
    
    try:
        print(compare_adjacent_numbers(list6))
    except TypeError as e:
        print(e)