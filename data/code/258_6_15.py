def average_pairs(list1, list2):
    return {list1[i]: (list1[i] + list2[i]) / 2 for i in range(len(list1))}

if __name__ == '__main__':
    print(average_pairs([1, 2, 3], [4, 5, 6]))