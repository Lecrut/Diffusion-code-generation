def find_largest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    
    largest = data[0]
    for element in data[1:]:
        if element > largest:
            largest = element
    
    return largest

if __name__ == '__main__':
    list1 = [1, 5, 2, 8, 3]
    print(f"List: {list1}, Largest: {find_largest(list1)}")
    
    list2 = [-10, -5, -20, -1]
    print(f"List: {list2}, Largest: {find_largest(list2)}")
    
    list3 = [42]
    print(f"List: {list3}, Largest: {find_largest(list3)}")