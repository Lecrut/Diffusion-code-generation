class MiddleElementFinder:
    @staticmethod
    def find_middle(sequence):
        n = len(sequence)
        if n == 0:
            return None
        middle_index = n // 2
        return sequence[middle_index]

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, 20, 30, 40, 50, 60]
    list3 = [1, 2, 3, 4]
    list4 = [100]
    list5 = []
    
    print("Middle of list1:", MiddleElementFinder.find_middle(list1))
    print("Middle of list2:", MiddleElementFinder.find_middle(list2))
    print("Middle of list3:", MiddleElementFinder.find_middle(list3))
    print("Middle of list4:", MiddleElementFinder.find_middle(list4))
    print("Middle of list5:", MiddleElementFinder.find_middle(list5))