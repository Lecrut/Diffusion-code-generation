class ListIntersector:
    @staticmethod
    def intersect(list1, list2):
        set1 = set(list1)
        set2 = set(list2)
        return list(set1 & set2)

if __name__ == '__main__':
    intersector = ListIntersector()
    list_a = [1, 2, 3, 4, 5]
    list_b = [4, 5, 6, 7, 8]
    result = intersector.intersect(list_a, list_b)
    print(result)

    list_c = ['apple', 'banana', 'cherry']
    list_d = ['banana', 'date', 'elderberry']
    result2 = intersector.intersect(list_c, list_d)
    print(result2)