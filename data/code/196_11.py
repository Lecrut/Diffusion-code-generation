def list_concatenator(list1, list2):
    return list1 + list2
if __name__ == '__main__':
    list_a = [1, 2, 3]
    list_b = ['a', 'b', 'c']
    result = list_concatenator(list_a, list_b)
    print(result)