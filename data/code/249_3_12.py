def find_largest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    return max(data)

if __name__ == '__main__':
    sample1 = [3, 5, 1, 2]
    sample2 = [-10, -5, -20, -1]
    sample3 = [42]
    sample4 = []
    
    print(f"Largest in {sample1}: {find_largest(sample1)}")
    print(f"Largest in {sample2}: {find_largest(sample2)}")
    print(f"Largest in {sample3}: {find_largest(sample3)}")
    try:
        find_largest(sample4)
    except ValueError as e:
        print(e)