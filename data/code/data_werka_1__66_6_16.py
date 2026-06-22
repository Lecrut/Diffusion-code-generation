class NumberListChecker:
    def __init__(self, data):
        self.data = data

    def is_sorted(self):
        n = len(self.data)
        if n <= 1:
            return True
        for i in range(n - 1):
            try:
                if not isinstance(self.data[i], (int, float)) or not isinstance(self.data[i+1], (int, float)):
                    raise TypeError(f"Non-numeric type found: {self.data[i]} and {self.data[i+1]}")
                if self.data[i] > self.data[i+1]:
                    return False
            except TypeError as e:
                print(e)
                return None
        return True

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [1, 'a', 2, 4, 5]
    list3 = [5, 4.0, 3, 2.5, 1]
    list4 = [1, 1, 2, 3, 3]
    list5 = [10]
    list6 = []

    checker1 = NumberListChecker(list1)
    checker2 = NumberListChecker(list2)
    checker3 = NumberListChecker(list3)
    checker4 = NumberListChecker(list4)
    checker5 = NumberListChecker(list5)
    checker6 = NumberListChecker(list6)

    print(f"List 1 is sorted: {checker1.is_sorted()}")
    print(f"List 2 is sorted: {checker2.is_sorted()}")
    print(f"List 3 is sorted: {checker3.is_sorted()}")
    print(f"List 4 is sorted: {checker4.is_sorted()}")
    print(f"List 5 is sorted: {checker5.is_sorted()}")
    print(f"List 6 is sorted: {checker6.is_sorted()}")