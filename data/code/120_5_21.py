def compare_values(x, y):
    if type(x) != type(y):
        raise TypeError(f"Type mismatch: Cannot directly compare {type(x)} and {type(y)}")
    
    if isinstance(x, int):
        result = x - y
    elif isinstance(x, str):
        result = (x > y) - (x < y)
    else:
        raise TypeError("Unsupported type for comparison")
    
    return result

if __name__ == '__main__':
    print("--- Integer Comparison ---")
    print(compare_values(10, 5))
    print(compare_values(20, 20))
    print(compare_values(3, 1))

    print("\n--- String Comparison ---")
    print(compare_values("apple", "banana"))
    print(compare_values("banana", "cherry"))
    print(compare_values("cherry", "apple"))