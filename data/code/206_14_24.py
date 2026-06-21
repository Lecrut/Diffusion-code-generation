min_value = lambda lst: min(lst) if lst else None

if __name__ == '__main__':
    sample1 = [3, 1, 4, 1, 5]
    sample2 = [7]
    sample3 = []
    
    def validate_sample(sample):
        if not isinstance(sample, list) or not all(isinstance(x, (int, float)) for x in sample):
            raise ValueError("Sample must be a list of numbers")
    
    validate_sample(sample1)
    validate_sample(sample2)
    validate_sample(sample3)
    
    print(f"Minimum in {sample1}: {min_value(sample1)}")
    print(f"Minimum in {sample2}: {min_value(sample2)}")
    print(f"Minimum in {sample3}: {min_value(sample3)}")