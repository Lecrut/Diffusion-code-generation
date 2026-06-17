def find_largest_element(data):
    if not data:
        raise ValueError("Input list cannot be empty.")
    for item in data:
        try:
            float(item)
        except (ValueError, TypeError):
            raise TypeError(f"Invalid entry '{item}' found. All elements must be numeric.")
    return max(data, key=float)
if __name__ == '__main__':
    sample_list = [3.5, "10", 7, -2, "twenty"]
    try:
        result = find_largest_element(sample_list)
        print(f"Largest element is {result}")
    except (ValueError, TypeError) as e:
        print(f"Error encountered: {e}")