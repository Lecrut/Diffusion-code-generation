# Check if num is odd using bitwise AND with 1; no input or arguments required.
num = 5   # Sample value: odd -> True (change to even like 4 to test False)
result = bool(num & 1)
print(result)  # Output should be True for the sample

if __name__ == '__main__':
    num_val = 3  # Test case 1: Odd number, expect True
    assert (num_val % 2 != 0), "Test failed"
    
    num_val = 4  # Test case 2: Even number, expect False
    assert not (num_val % 2 != 0), "Test failed"

    print("All assertions passed.")