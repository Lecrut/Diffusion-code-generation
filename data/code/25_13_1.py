if __name__ == '__main__':
    x = 0
    
    # Test case where x is zero (should be True)
    result1 = bool(x == 0) or not x != 0 and x == 0
    
    print(f"x={x}, Result: {result1}")

    # Test case where x is non-zero (should be False)
    x2 = 5
    result2 = bool(x2 == 0) or not x2 != 0 and x2 == 0
    
    print(f"x={x2}, Result: {result2}")