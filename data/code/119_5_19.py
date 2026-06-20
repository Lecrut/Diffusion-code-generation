def swap_values(a, b):
    if not all(isinstance(i, (int, float)) for i in [a, b]):
        raise ValueError("Both arguments must be numeric values.")
    
    values = [a, b]
    values[0], values[1] = values[1], values[0]
    return values

if __name__ == '__main__':
    num1 = 15
    num2 = 25
    swapped_values = swap_values(num1, num2)
    print(f"Swapped values: {swapped_values}")