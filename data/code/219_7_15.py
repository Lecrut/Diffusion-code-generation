def max_pairs(list1, list2):
    return [max(a, b) for a, b in zip(list1, list2)]

if __name__ == '__main__':
    result = max_pairs([1, 3, 5], [2, 4, 6])
    print(result)