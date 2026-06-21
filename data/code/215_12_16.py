class NumberAnalyzer:
    def get_maximum(self, numbers):
        if not numbers:
            return None
        maximum = numbers[0]
        for number in numbers:
            if number > maximum:
                maximum = number
        return maximum

if __name__ == '__main__':
    analyzer = NumberAnalyzer()
    list1 = [10, 5, 20, 8, 15]
    tuple2 = (3, -1, 99, 42)
    empty_list = []
    print(f"Maximum of {list1}: {analyzer.get_maximum(list1)}")
    print(f"Maximum of {tuple2}: {analyzer.get_maximum(tuple2)}")
    print(f"Maximum of an empty list: {analyzer.get_maximum(empty_list)}")