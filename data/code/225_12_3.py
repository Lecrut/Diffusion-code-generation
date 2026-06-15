class MinMaxFinder:
    def compare_values(self, list1, list2):
        min1 = min(list1) if list1 else None
        max1 = max(list1) if list1 else None
        min2 = min(list2) if list2 else None
        max2 = max(list2) if list2 else None
        return {
            "list1": {"min": min1, "max": max1},
            "list2": {"min": min2, "max": max2}
        }
if __name__ == '__main__':
    finder = MinMaxFinder()
    list_a = [10, 5, 20, 15]
    list_b = [3, 8, 1, 12]
    result = finder.compare_values(list_a, list_b)
    print(result)