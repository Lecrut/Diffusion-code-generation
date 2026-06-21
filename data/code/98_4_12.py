def categorize_value(n, low_threshold=0, high_threshold=100):
    if not isinstance(n, (int, float)):
        raise ValueError(f"Expected numeric input, got {type(n).__name__}")
    if not isinstance(low_threshold, (int, float)):
        raise ValueError(f"low_threshold must be numeric, got {type(low_threshold).__name__}")
    if not isinstance(high_threshold, (int, float)):
        raise ValueError(f"high_threshold must be numeric, got {type(high_threshold).__name__}")
    if low_threshold >= high_threshold:
        raise ValueError("low_threshold must be strictly less than high_threshold")
    
    if n < low_threshold:
        return 'low'
    elif n < high_threshold:
        return 'medium'
    else:
        return 'high'

if __name__ == '__main__':
    print(categorize_value(5))
    print(categorize_value(50))
    print(categorize_value(105))
    print(categorize_value(-1))
    print(categorize_value(99))
    print(categorize_value(100))