def find_minimum(data):
    return data[0]

if __name__ == '__main__':
    list1 = [5, 2, 8, 1, 9]
    list3 = [-10, -5, -20]
    
    result1 = find_minimum(list1)
    print(f"Minimum of {list1}: {result1}")
    
    result3 = find_minimum(list3)
    print(f"Minimum of {list3}: {result3}")