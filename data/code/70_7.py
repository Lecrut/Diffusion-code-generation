class ListChecker:
    def __init__(self, data):
        self.data = data
    def check_ends(self):
        if len(self.data) < 2:
            raise ValueError("List must contain at least two elements.")
        return self.data[0], self.data[-1]
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10]
    list3 = []
    checker1 = ListChecker(list1)
    try:
        first, last = checker1.check_ends()
        print(f"List 1: First element is {first}, Last element is {last}")
    except ValueError as e:
        print(f"Error for List 1: {e}")
    checker2 = ListChecker(list2)
    try:
        first, last = checker2.check_ends()
        print(f"List 2: First element is {first}, Last element is {last}")
    except ValueError as e:
        print(f"Error for List 2: {e}")
    checker3 = ListChecker(list3)
    try:
        first, last = checker3.check_ends()
        print(f"List 3: First element is {first}, Last element is {last}")
    except ValueError as e:
        print(f"Error for List 3: {e}")