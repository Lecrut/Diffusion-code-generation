from collections import OrderedDict
def remove_duplicates(lst):
    return list(OrderedDict.fromkeys(lst))
if __name__ == '__main__':
    data = [3, 1, 4, 5, 9, 2, 6, 8, 0, -1] * 2 + [7]
    result = remove_duplicates(data)
    print(result)