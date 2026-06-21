min_value = lambda lst: min(lst) if lst else None

if __name__ == '__main__':
    sample1 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    sample2 = [-2, -1, 0]
    sample3 = []
    
    print(f"Minimum in {sample1}: {min_value(sample1)}")
    print(f"Minimum in {sample2}: {min_value(sample2)}")
    print(f"Minimum in {sample3}: {min_value(sample3)}")