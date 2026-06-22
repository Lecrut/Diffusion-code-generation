def get_penultimate_item(items):
    if len(items) < 2:
        raise ValueError("List must contain at least two elements")
    return items[-2]

if __name__ == '__main__':
    sample_list_1 = [10, 20, 30, 40, 50]
    sample_list_2 = ['apple', 'banana', 'cherry']
    sample_list_3 = [42]
    try:
        result1 = get_penultimate_item(sample_list_1)
        print(result1)
        result2 = get_penultimate_item(sample_list_2)
        print(result2)
        result3 = get_penultimate_item(sample_list_3)
        print(result3)
    except ValueError as e:
        print(f"Error: {e}")