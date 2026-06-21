def concatenate_lists_generator(list1, list2):
    for item in list1:
        yield item
    for item in list2:
        yield item

if __name__ == '__main__':
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    concatenated_generator = concatenate_lists_generator(list1, list2)
    result = []
    for _ in range(len(list1) + len(list2)):
        result.append(next(concatenated_generator))
    print(result)