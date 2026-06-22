def second_to_last_item(lst):
    if not lst or len(lst) < 2:
        raise ValueError("List must have at least two items")
    return lst[-2]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = second_to_last_item(sample_list)
    print(result)