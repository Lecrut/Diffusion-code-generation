def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    minimum = float('inf')
    for number in data:
        if number < minimum:
            minimum = number
    return minimum

if __name__ == '__main__':
    sample1 = [3.14, 1.618, 2.718, 0.577]
    sample2 = [-10.5, 5.2, -3.14, 9.9]
    sample3 = [42.0]
    empty_list = []
    
    print(f"Minimum of {sample1}: {find_minimum(sample1)}")
    print(f"Minimum of {sample2}: {find_minimum(sample2)}")
    print(f"Minimum of {sample3}: {find_minimum(sample3)}")
    try:
        find_minimum(empty_list)
    except ValueError as e:
        print(e)