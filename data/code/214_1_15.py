class MinFinder:
    @staticmethod
    def find_minimum(numbers):
        if not numbers:
            return None
        minimum = numbers[0]
        for number in numbers:
            if number < minimum:
                minimum = number
        return minimum

if __name__ == '__main__':
    list1 = [5, 2, 8, 1, 9]
    list2 = [-10, 0, 50, -3]
    list3 = []
    list4 = [42]
    print(f"Minimum of {list1}: {MinFinder.find_minimum(list1)}")
    print(f"Minimum of {list2}: {MinFinder.find_minimum(list2)}")
    print(f"Minimum of {list3}: {MinFinder.find_minimum(list3)}")
    print(f"Minimum of {list4}: {MinFinder.find_minimum(list4)}")