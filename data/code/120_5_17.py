def compare_values(x, y):
    if type(x) != type(y):
        return f"Type mismatch: Cannot directly compare {type(x)} and {type(y)}"
    
    if x < y:
        return f"{x} is less than {y}"
    elif x > y:
        return f"{x} is greater than {y}"
    else:
        return f"{x} is equal to {y}"

if __name__ == '__main__':
    print("--- String Comparison ---")
    result = compare_values("apple", "banana")
    print(result)
    
    print("\n--- Integer Comparison ---")
    result = compare_values(10, 5)
    print(result)