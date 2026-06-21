class JaccardComparator:
    def calculate_jaccard_similarity(self, list1, list2):
        set1 = set(list1)
        set2 = set(list2)
        intersection = set1.intersection(set2)
        union = set1.union(set2)
        return len(intersection) / len(union)

if __name__ == '__main__':
    comparator = JaccardComparator()
    list_a = [1, 2, 3, 4, 5]
    list_b = [4, 5, 6, 7, 8]
    similarity = comparator.calculate_jaccard_similarity(list_a, list_b)
    print(similarity)