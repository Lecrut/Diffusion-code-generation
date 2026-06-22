def sort_three_numbers(a, b, c):
    if not all(isinstance(i, int) for i in [a, b, c]):
        raise ValueError("All arguments must be integers.")
    
    smallest = min(a, b, c)
    largest = max(a, b, c)
    middle = a + b + c - smallest - largest
    
    return (smallest, middle, largest)

if __name__ == '__main__':
    print(sort_three_numbers(3, 1, 2))