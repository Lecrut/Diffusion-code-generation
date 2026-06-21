def reverse_list(arr):
    if not isinstance(arr, list):
        raise ValueError("Input must be a list")
    
    return arr[::-1]

if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7]
    print("Original list:", data)
    print("Reversed list:", reverse_list(data))
    
    data2 = [10, 20, 30, 40, 50]
    print("Original list:", data2)
    print("Reversed list:", reverse_list(data2))
    
    data3 = [1, 2, 1, 3, 5, 4]
    print("Original list:", data3)
    print("Reversed list:", reverse_list(data3))