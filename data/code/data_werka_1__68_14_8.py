class SymmetricDifference:
    @staticmethod
    def _unique_elements(iterable):
        seen = set()
        unique_elements = []
        for item in iterable:
            if item not in seen:
                unique_elements.append(item)
                seen.add(item)
        return unique_elements

    @staticmethod
    def symmetric_difference(iterable1, iterable2):
        unique1 = SymmetricDifference._unique_elements(iterable1)
        unique2 = SymmetricDifference._unique_elements(iterable2)

        diff_set1 = set(unique1) - set(unique2)
        diff_set2 = set(unique2) - set(unique1)
        
        return list(diff_set1.union(diff_set2))

if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    list_b = [4, 5, 6, 7, 8]
    result = SymmetricDifference.symmetric_difference(list_a, list_b)
    print(result)