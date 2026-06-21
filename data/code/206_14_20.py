min_value = lambda lst: min(lst) if lst else None

if __name__ == '__main__':
    sample1 = [3, 1, 4, 1, 5]
    sample2 = [7]
    sample3 = [-3, -1, -4, -1, -5]
    
    print(f"Minimum in {sample1}: {min_value(sample1)}")
    print(f"Minimum in {sample2}: {min_value(sample2)}")
    print(f"Minimum in {sample3}: {min_value(sample3)}")