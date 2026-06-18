class ListComparator:
    def compare_and_return(self, list1, list2):
        sum1 = sum(list1)
        sum2 = sum(list2)
        if sum1 > sum2:
            return list1
        elif sum2 > sum1:
            return list2
        else:
            return list1
if __name__ == '__main__':
    comparator = ListComparator()
    list_a = [1, 5, 3]
    list_b = [2, 4, 1]
    result = comparator.compare_and_return(list_a, list_b)
    print(result)