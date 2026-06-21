class JaccardIndexCalculator:
    @staticmethod
    def compute_intersection(list1, list2):
        set1 = set(list1)
        set2 = set(list2)
        return set1.intersection(set2)

    @staticmethod
    def compute_union(list1, list2):
        set1 = set(list1)
        set2 = set(list2)
        return set1.union(set2)

    @classmethod
    def calculate_jaccard_similarity(cls, list1, list2):
        intersection = cls.compute_intersection(list1, list2)
        union = cls.compute_union(list1, list2)
        if len(union) == 0:
            return 0.0
        return len(intersection) / len(union)

if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    list_b = [4, 5, 6, 7, 8]
    calculator = JaccardIndexCalculator()
    similarity = calculator.calculate_jaccard_similarity(list_a, list_b)
    print(similarity)