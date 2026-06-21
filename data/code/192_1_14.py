class ListIntersection:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def intersect(self):
        result = []
        i, j = 0, 0
        while i < len(self.list1) and j < len(self.list2):
            if self.list1[i] == self.list2[j]:
                result.append(self.list1[i])
                i += 1
                j += 1
            elif self.list1[i] < self.list2[j]:
                i += 1
            else:
                j += 1
        return result

if __name__ == '__main__':
    sample_list1 = [1, 3, 5, 7, 9]
    sample_list2 = [0, 2, 4, 6, 8, 9]
    intersection = ListIntersection(sample_list1, sample_list2)
    print(intersection.intersect())