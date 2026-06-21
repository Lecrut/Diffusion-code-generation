def find_smallest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    smallest = data[0]
    for element in data[1:]:
        if element < smallest:
            smallest = element
    return smallest

if __name__ == '__main__':
    sample_list1 = [3.5, 2.1, 8.7, 1.9, 9.2]
    print(f"The smallest element in {sample_list1} is: {find_smallest(sample_list1)}")
    
    sample_list2 = [-10.5, 0.2, -5.3, 3.4]
    print(f"The smallest element in {sample_list2} is: {find_smallest(sample_list2)}")
    
    sample_list3 = [42.7]
    print(f"The smallest element in {sample_list3} is: {find_smallest(sample_list3)}")
    
    sample_list4 = [100.1, 50.6, 25.3, 75.9]
    print(f"The smallest element in {sample_list4} is: {find_smallest(sample_list4)}")