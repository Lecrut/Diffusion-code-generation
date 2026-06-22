def validate_input(data):
    if not data:
        raise ValueError("Input list cannot be empty")

def find_min_max(data):
    validate_input(data)
    minimum = min(data)
    maximum = max(data)
    return (minimum, maximum)

if __name__ == '__main__':
    list1 = [3.5, 1.2, 4.8, 1.9, 5.7, 9.1, 2.3]
    result1 = find_min_max(list1)
    print(f"List: {list1}, Min: {result1[0]}, Max: {result1[1]}")
    
    list2 = [-10.5, 0.0, 5.6, -20.3, 100.4]
    result2 = find_min_max(list2)
    print(f"List: {list2}, Min: {result2[0]}, Max: {result2[1]}")