def find_largest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    largest = max(data)
    return largest

if __name__ == '__main__':
    sample1 = [4, 9, 2, 6, 5]
    sample2 = [-3, -7, -1, -8]
    sample3 = [0]
    empty_list = []
    
    print(f"Largest in {sample1}: {find_largest(sample1)}")
    print(f"Largest in {sample2}: {find_largest(sample2)}")
    print(f"Largest in {sample3}: {find_largest(sample3)}")
    try:
        find_largest(empty_list)
    except ValueError as e:
        print(e)