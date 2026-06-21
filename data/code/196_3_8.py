def append_lists(list_a, list_b):
    if not isinstance(list_a, list) or not isinstance(list_b, list):
        raise ValueError("Both arguments must be lists")
    
    for item in list_b:
        list_a.append(item)

if __name__ == '__main__':
    list_a = [1, 2, 3]
    list_b = [4, 5, 6]
    append_lists(list_a, list_b)
    print(f"Updated list A: {list_a}")