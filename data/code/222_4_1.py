def process_list(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    return sum(data)
if __name__ == '__main__':
    list1 = [1, 2, 3]
    list2 = []
    try:
        result1 = process_list(list1)
        print(f"Result for {list1}: {result1}")
        result2 = process_list(list2)
        print(f"Result for {list2}: {result2}")
    except ValueError as e:
        print(f"Error caught: {e}")