class ListChecker:
    def __init__(self, data):
        self.data = data
    def check_ends(self):
        if len(self.data) < 2:
            raise ValueError("List must contain at least two elements to check the first and last.")
        return self.data[0], self.data[-1]
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10]
    list3 = []
    list4 = ['a', 'b']
    checker1 = ListChecker(list1)
    print(f"List1 check: {checker1.check_ends()}")
    checker2 = ListChecker(list2)
    try:
        checker2.check_ends()
    except ValueError as e:
        print(f"List2 check failed: {e}")
    checker3 = ListChecker(list3)
    try:
        checker3.check_ends()
    except ValueError as e:
        print(f"List3 check failed: {e}")
    checker4 = ListChecker(list4)
    print(f"List4 check: {checker4.check_ends()}")