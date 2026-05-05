class ListChecker:
    def __init__(self, data):
        self.data = data
    def check_ends(self):
        if len(self.data) < 2:
            raise ValueError("List must contain at least two elements.")
        first = self.data[0]
        last = self.data[-1]
        return first, last
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = ['a', 'b']
    list3 = [10]
    list4 = []
    checker1 = ListChecker(list1)
    print(f"List 1 check: {checker1.check_ends()}")
    checker2 = ListChecker(list2)
    print(f"List 2 check: {checker2.check_ends()}")
    try:
        checker3 = ListChecker(list3)
        checker3.check_ends()
    except ValueError as e:
        print(f"List 3 error: {e}")
    try:
        checker4 = ListChecker(list4)
        checker4.check_ends()
    except ValueError as e:
        print(f"List 4 error: {e}")