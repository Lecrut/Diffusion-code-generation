def find_min_max(data):
    if not data:
        return None, None
    
    smallest = largest = data[0]
    
    for number in data[1:]:
        if number < smallest:
            smallest = number
        elif number > largest:
            largest = number
            
    return smallest, largest

if __name__ == '__main__':
    large_list = [45, 12, 89, 3, 67, 22, 91, 50, 1]
    min_val, max_val = find_min_max(large_list)
    print(f"The list is: {large_list}")
    print(f"Smallest element: {min_val}")
    print(f"Largest element: {max_val}")