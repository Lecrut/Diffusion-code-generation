def fetch_element(lst, index):
    if index < 0 or index >= len(lst):
        raise ValueError("Index out of bounds")
    return lst[index]

if __name__ == '__main__':
    example_list = [7, 14, 21, 28, 35]
    position_to_fetch = 2
    try:
        result = fetch_element(example_list, position_to_fetch)
        print(result)
    except ValueError as e:
        print(e)