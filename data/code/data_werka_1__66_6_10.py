class NumberList:
    def __init__(self, data):
        self.data = data

    def compare_adjacent(self):
        for i in range(len(self.data) - 1):
            if not isinstance(self.data[i], (int, float)) or not isinstance(self.data[i+1], (int, float)):
                raise TypeError("Non-numeric adjacent elements found")
            if self.data[i] > self.data[i+1]:
                return False
        return True

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [1, 'a', 3, 4, 5]
    list3 = [5.0, 4.5, 3.0, 2.0, 1.0]
    list4 = [1, 1, 2, 3, 3]

    try:
        nl1 = NumberList(list1)
        print(f"List 1 is sorted: {nl1.compare_adjacent()}")
    except TypeError as e:
        print(e)

    try:
        nl2 = NumberList(list2)
        print(f"List 2 is sorted: {nl2.compare_adjacent()}")
    except TypeError as e:
        print(e)

    try:
        nl3 = NumberList(list3)
        print(f"List 3 is sorted: {nl3.compare_adjacent()}")
    except TypeError as e:
        print(e)

    try:
        nl4 = NumberList(list4)
        print(f"List 4 is sorted: {nl4.compare_adjacent()}")
    except TypeError as e:
        print(e)