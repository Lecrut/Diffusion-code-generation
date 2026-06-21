def concatenate_lists_gen(list1, list2):
    yield from list1
    yield from list2

if __name__ == '__main__':
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    concatenated_gen = concatenate_lists_gen(list1, list2)
    print("Concatenated list:")
    for item in concatenated_gen:
        print(item, end=' ')