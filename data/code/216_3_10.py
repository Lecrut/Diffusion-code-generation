class DataAnalyzer:
    def __init__(self, data):
        self.data = data

    def find_middle(self):
        n = len(self.data)
        if n == 0:
            return None
        elif n % 2 == 1:
            middle_index = n // 2
            return self.data[middle_index]
        else:
            middle_right_index = n // 2
            middle_left_index = middle_right_index - 1
            middle_value = (self.data[middle_left_index] + self.data[middle_right_index]) / 2.0
            return middle_value

if __name__ == '__main__':
    analyzer1 = DataAnalyzer([1, 2, 3, 4, 5])
    analyzer2 = DataAnalyzer([10, 20, 30, 40])
    analyzer3 = DataAnalyzer([1, 2])
    analyzer4 = DataAnalyzer([1, 2, 3])

    print(f"Middle of {analyzer1.data}: {analyzer1.find_middle()}")
    print(f"Middle of {analyzer2.data}: {analyzer2.find_middle()}")
    print(f"Middle of {analyzer3.data}: {analyzer3.find_middle()}")
    print(f"Middle of {analyzer4.data}: {analyzer4.find_middle()}")