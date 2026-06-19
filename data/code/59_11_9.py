class MiddleFinder:
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

    print("List 1:", MiddleFinder.find_middle(list1))
    print("List 2:", MiddleFinder.find_middle(list2))
    print("List 3:", MiddleFinder.find_middle(list3))
    print("List 4:", MiddleFinder.find_middle(list4))
    print("List 5:", MiddleFinder.find_middle(list5))