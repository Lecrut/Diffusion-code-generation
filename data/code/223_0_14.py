def find_max_value(numbers):
    return max(numbers)

if __name__ == '__main__':
    sample1 = [3, 1, 4, 1, 5, 9, 2]
    print(f"Maximum of {sample1}: {find_max_value(sample1)}")
    
    sample2 = [-10, -5, -20, -1]
    print(f"Maximum of {sample2}: {find_max_value(sample2)}")
    
    sample3 = [7]
    print(f"Maximum of {sample3}: {find_max_value(sample3)}")