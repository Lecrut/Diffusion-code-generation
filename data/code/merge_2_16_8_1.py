def count_elements(lst):
    return len(lst)
if __name__ == '__main__':
    data = [1, "apple", 3.5, None]
    print(count_elements(data))
    empty_list = []
    print(count_elements(empty_list))
    mixed_types = ["a", True, {}, [], 42]
    print(count_elements(mixed_types))