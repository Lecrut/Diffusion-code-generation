def compare_min_max(list1, list2):
    try:
        min_list1 = min(list1)
        max_list1 = max(list1)
        min_list2 = min(list2)
        max_list2 = max(list2)

        return (min_list1, max_list1), (min_list2, max_list2)
    except ValueError as e:
        raise ValueError("Lists must contain at least one number") from e
    except TypeError as e:
        raise TypeError("Inputs must be lists of numbers") from e

if __name__ == '__main__':
    list_a = [3.14, 1.618, 2.718]
    list_b = [-10.5, 5.2, 0.0]

    min_max_a, min_max_b = compare_min_max(list_a, list_b)

    print(f"List A: {list_a}")
    print(f"Min and Max of List A: {min_max_a}")

    print(f"List B: {list_b}")
    print(f"Min and Max of List B: {min_max_b}")