def find_min_max(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    minimum = min(data)
    maximum = max(data)
    return (minimum, maximum)

if __name__ == '__main__':
    sample_list1 = [3.5, 2.1, 4.8, 1.9, 5.6, 9.0, 2.7]
    result1 = find_min_max(sample_list1)
    print(f"List: {sample_list1}, Min: {result1[0]}, Max: {result1[1]}")
    
    sample_list2 = [-10.2, 0.5, 5.3, -20.7, 100.1]
    result2 = find_min_max(sample_list2)
    print(f"List: {sample_list2}, Min: {result2[0]}, Max: {result2[1]}")