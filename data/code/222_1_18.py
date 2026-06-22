SMALLER_THAN = lambda x, y: x < y

def find_smallest(lst):
    if not lst:
        raise ValueError("Input list cannot be empty")
    
    smallest = lst[0]
    for num in lst[1:]:
        if SMALLER_THAN(num, smallest):
            smallest = num
    return smallest

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(find_smallest(sample_list))