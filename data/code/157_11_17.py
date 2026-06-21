def find_smallest(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    smallest = float('inf')
    for number in numbers:
        if number < smallest:
            smallest = number
    
    return smallest

if __name__ == '__main__':
    LIST_1 = [3, 1, 4, 1, 5, 9, 2]
    LIST_2 = [-10, 5, 0, -3, 12]
    LIST_3 = [42]
    LIST_4 = [7]
    
    print(f"Smallest in {LIST_1}: {find_smallest(LIST_1)}")
    print(f"Smallest in {LIST_2}: {find_smallest(LIST_2)}")
    print(f"Smallest in {LIST_3}: {find_smallest(LIST_3)}")
    print(f"Smallest in {LIST_4}: {find_smallest(LIST_4)}")