import sys

if __name__ == '__main__':
    # Test with various negative and non-negative values
    test_values = [-5, 0, 3]
    
    print("-" * 40)
    for val in test_values:
        result = x < 0 if (x := val) else None
        
        print(f"x={val} -> {result}")