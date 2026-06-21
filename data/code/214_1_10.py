class MinFinder:
    def __init__(self):
        self.min_value = None

    def update_min(self, number):
        if self.min_value is None or number < self.min_value:
            self.min_value = number

def find_minimum(numbers):
    finder = MinFinder()
    for number in numbers:
        finder.update_min(number)
    return finder.min_value

if __name__ == '__main__':
    list1 = [5, 2, 8, 1, 9]
    list2 = [-10, 0, 50, -3]
    list3 = []
    list4 = [42]
    print(f"Minimum of {list1}: {find_minimum(list1)}")
    print(f"Minimum of {list2}: {find_minimum(list2)}")
    print(f"Minimum of {list3}: {find_minimum(list3)}")
    print(f"Minimum of {list4}: {find_minimum(list4)}")