def average_pairs(list1, list2):
    return {list1[i]: (list1[i] + list2[i]) / 2 for i in range(min(len(list1), len(list2)))}

if __name__ == '__main__':
    print(average_pairs([10, 20, 30], [40, 50, 60]))