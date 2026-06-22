def find_min_max(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    minimum = data[0]
    maximum = data[0]
    for x in data:
        if x < minimum:
            minimum = x
        if x > maximum:
            maximum = x
    return (minimum, maximum)

if __name__ == '__main__':
    sample_list1 = [7.5, 3.2, 9.8, 1.4, 6.3]
    result1 = find_min_max(sample_list1)
    print(f"List: {sample_list1}, Min: {result1[0]}, Max: {result1[1]}")
    
    sample_list2 = [-5.1, 2.7, -3.4, 8.9, 0.0]
    result2 = find_min_max(sample_list2)
    print(f"List: {sample_list2}, Min: {result2[0]}, Max: {result2[1]}")