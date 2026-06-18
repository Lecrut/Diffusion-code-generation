def find_largest_element(data):
    for item in data:
        if not isinstance(item, (int, float)):
            raise TypeError(f"Invalid entry {item} is not a number.")
    return max(data)
if __name__ == '__main__':
    sample_list = [3.5, 10, "invalid", -2]
    try:
        result = find_largest_element(sample_list)
        print(f"Largest element: {result}")
    except TypeError as e:
        print(f"Error: {e}")