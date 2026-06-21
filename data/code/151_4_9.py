def combine_lists(list1, list2):
    try:
        return list(zip(list1, list2))
    except TypeError as e:
        return [f"Error: {e}"]

if __name__ == '__main__':
    list_a = [1, 2, 3]
    list_b = ['a', 'b', 'c']
    result = combine_lists(list_a, list_b)
    print(f"Combination of {list_a} and {list_b}: {result}")