def is_odd(n):
    return n & 1 == 1

if __name__ == '__main__':
    test_value_1 = 7
    test_value_2 = 8
    
    print(f"Testing with odd number {test_value_1}:")
    if is_odd(test_value_1):
        print("Result: Odd")
    else:
        print("Result: Even")
    
    print(f"\nTesting with even number {test_value_2}:")
    if is_odd(test_value_2):
        print("Result: Odd")
    else:
        print("Result: Even")