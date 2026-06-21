min_value = lambda lst: min(lst) if lst else None

def find_min_value(lst):
    if not isinstance(lst, list):
        raise ValueError("Input must be a list")
    for item in lst:
        if not isinstance(item, (int, float)):
            raise ValueError("List items must be numbers")
    return min_value(lst)

if __name__ == '__main__':
    sample1 = [3, 1, 4, 1, 5]
    sample2 = [7]
    sample3 = []
    print(f"Minimum in {sample1}: {find_min_value(sample1)}")
    print(f"Minimum in {sample2}: {find_min_value(sample2)}")
    try:
        print(find_min_value(sample3))
    except ValueError as e:
        print(e)