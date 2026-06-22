class MinFinder:
    def __init__(self):
        self.min_value = float('inf')

    def update_min(self, number):
        if number < self.min_value:
            self.min_value = number

def find_minimum(numbers):
    finder = MinFinder()
    for num in numbers:
        finder.update_min(num)
    return finder.min_value

if __name__ == '__main__':
    data1 = [3, 1, 4, 1, 5, 9, 2]
    result1 = find_minimum(data1)
    print(result1)

    data2 = [-10, 0, 5, -20, 3]
    result2 = find_minimum(data2)
    print(result2)

    data3 = [42]
    result3 = find_minimum(data3)
    print(result3)