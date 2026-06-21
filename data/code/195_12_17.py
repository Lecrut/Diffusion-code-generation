def compare_elements(a, b):
    if a == b:
        return True
    elif isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            return False
        for item1, item2 in zip(a, b):
            if not compare_elements(item1, item2):
                return False
        return True
    else:
        return False

if __name__ == '__main__':
    list_a = [1, [2, 3], 4]
    list_b = [1, [2, 3], 4]
    list_c = [1, [2, 4], 4]
    print(f"Comparing {list_a} and {list_b}: {compare_elements(list_a, list_b)}")
    print(f"Comparing {list_a} and {list_c}: {compare_elements(list_a, list_c)}")