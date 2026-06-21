class LargestFinder:
    def find_largest(self, data):
        if not data:
            return None
        max_value = float('-inf')
        for value in data:
            if isinstance(value, (int, float)) and value > max_value:
                max_value = value
        return max_value

if __name__ == '__main__':
    finder = LargestFinder()
    list1 = [3, 1, 4, 1, 5, 9, 2]
    print(finder.find_largest(list1))
    list2 = [-10, -5, -20, -1]
    print(finder.find_largest(list2))