def find_maximum(strings):
    if not strings:
        raise ValueError("Input list cannot be empty")
    return max(strings)

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date"]
    try:
        maximum = find_maximum(sample_list)
        print(maximum)
    except ValueError as e:
        print(f"Error: {e}")