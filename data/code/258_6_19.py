def average_pairs(list1, list2):
    return {pair[0]: (pair[1] + pair[2]) / 2 for pair in zip(list1, list2)}

if __name__ == '__main__':
    print(average_pairs([1, 2, 3], [4, 5, 6]))