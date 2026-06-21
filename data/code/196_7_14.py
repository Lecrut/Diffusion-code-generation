def concatenate_lists(list1, list2):
    for item in list1:
        yield item
    for item in list2:
        yield item

if __name__ == '__main__':
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    concatenated = concatenate_lists(list1, list2)
    print(list(concatenated))