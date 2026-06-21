class MaxIndexFinder:
    def find_max_index(self, numbers):
        max_value = float('-inf')
        max_index = -1
        for index, number in enumerate(numbers):
            if number > max_value:
                max_value = number
                max_index = index
        return max_index

if __name__ == '__main__':
    finder = MaxIndexFinder()
    numbers = [3, 5, 2, 8, 1]
    result = finder.find_max_index(numbers)
    print(result)