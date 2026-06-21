def append_lists_in_place(list_a, list_b):
    for item in list_b:
        list_a.append(item)

if __name__ == '__main__':
    list_a = [1, 2, 3]
    list_b = [4, 5, 6]
    append_lists_in_place(list_a, list_b)
    print(f"Merged list: {list_a}")