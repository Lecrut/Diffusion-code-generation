class ListOperations:
    INTERSECTION = 1
    UNION = 2
    DIFFERENCE = 3

    @staticmethod
    def apply_operation(list1, list2, operation):
        if operation == ListOperations.INTERSECTION:
            return set(list1).intersection(set(list2))
        elif operation == ListOperations.UNION:
            return set(list1).union(set(list2))
        elif operation == ListOperations.DIFFERENCE:
            return set(list1) - set(list2)
        else:
            raise ValueError('Invalid operation')
if __name__ == '__main__':
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]
    operation = ListOperations.INTERSECTION
    result = ListOperations.apply_operation(list1, list2, operation)
    print(result)