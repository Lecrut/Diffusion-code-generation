def average_pairs(list1, list2):
    return {list1[i]: list2[i] for i in range(min(len(list1), len(list2)))}

if __name__ == '__main__':
    result = average_pairs([1, 2, 3], [4, 5, 6])
    print(result)