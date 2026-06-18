def count_elements(lst):
    return len(lst)
if __name__ == '__main__':
    data = [1, "apple", 3.5, None, True]
    result = count_elements(data)
    print(result)
    empty_data = []
    print(count_elements(empty_data))