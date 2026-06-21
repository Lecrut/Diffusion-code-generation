def find_largest(data):
    if not data:
        return None
    largest = data[0]
    for number in data:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_list1 = [-7, -3, -4, -1, -5, -9, -2]
    print(f"List: {sample_list1}, Largest element: {find_largest(sample_list1)}")
    
    sample_list2 = [3, 1, 4, 1, 5, 9, 2]
    print(f"List: {sample_list2}, Largest element: {find_largest(sample_list2)}")
    
    sample_list3 = [-10, -5, -20, -1]
    print(f"List: {sample_list3}, Largest element: {find_largest(sample_list3)}")
    
    sample_list4 = [7]
    print(f"List: {sample_list4}, Largest element: {find_largest(sample_list4)}")
    
    sample_list5 = []
    print(f"List: {sample_list5}, Largest element: {find_largest(sample_list5)}")