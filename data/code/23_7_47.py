class ListComparer:
    @staticmethod
    def calculate_sum(lst):
        return sum(lst)

    @classmethod
    def compare_and_report(cls, list1, list2):
        if not all(isinstance(x, int) for x in list1 + list2):
            raise ValueError("All elements in both lists must be integers.")
        
        sum1 = cls.calculate_sum(list1)
        sum2 = cls.calculate_sum(list2)
        
        if sum1 > sum2:
            return sum1, list1
        elif sum2 > sum1:
            return sum2, list2
        else:
            return sum1, None

if __name__ == '__main__':
    list_a = [10, 20, 30]
    list_b = [5, 5, 5, 50]
    result = ListComparer.compare_and_report(list_a, list_b)
    print(result)