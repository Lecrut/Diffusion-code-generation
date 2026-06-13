class ListUtils:
    @staticmethod
    def concatenate(list1, list2):
        return list1 + list2
if __name__ == '__main__':
    list_a = [1, 2, 3]
    list_b = [4, 5, 6]
    result = ListUtils.concatenate(list_a, list_b)
    print(result)
    print(f"List A after operation: {list_a}")
    print(f"List B after operation: {list_b}")