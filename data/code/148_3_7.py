def find_largest(data):
    if not data:
        raise ValueError("List cannot be empty")
    return max(data)

if __name__ == '__main__':
    sample_values = [
        [10, 5, 20, 8],
        [-5, -1, -10, -2],
        [3.14, 2.71, 1.618],
        [42]
    ]
    
    for values in sample_values:
        print(f"Largest in {values}: {find_largest(values)}")