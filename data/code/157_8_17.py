def find_smallest(data):
    if not data:
        raise ValueError("List cannot be empty")
    return min(data)

if __name__ == '__main__':
    sample_values = ["banana", "apple", "cherry"]
    try:
        smallest = find_smallest(sample_values)
        print(smallest)
    except ValueError as e:
        print(e)