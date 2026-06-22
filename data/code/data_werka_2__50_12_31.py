class ElementwiseDifferenceCalculator:
    @staticmethod
    def _merge_with_difference(list1, list2):
        result = []
        i, j = 0, 0
        while i < len(list1) and j < len(list2):
            if list1[i] == list2[j]:
                i += 1
                j += 1
            elif list1[i] < list2[j]:
                result.append(list1[i])
                i += 1
            else:
                result.append(list2[j])
                j += 1
        return result + list1[i:] + list2[j:]

    @staticmethod
    def calculate_difference(list1, list2):
        return ElementwiseDifferenceCalculator._merge_with_difference(list1, list2)

if __name__ == '__main__':
    sample_list1 = [1, 3, 5, 7, 9]
    sample_list2 = [2, 3, 6, 8, 10]
    difference = ElementwiseDifferenceCalculator.calculate_difference(sample_list1, sample_list2)
    print(difference)