def find_middle(data):
    n = len(data)
    if n == 0:
        raise ValueError("List is empty")
    middle_index = (n - 1) // 2
    return data[middle_index]

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    try:
        result = find_middle(sample_values)
        print(f"Middle value: {result}")
    except ValueError as e:
        print(e)