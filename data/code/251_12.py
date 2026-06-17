class NumberAnalyzer:
    def get_maximum(self, data):
        if not data:
            raise ValueError("Input iterable cannot be empty")
        maximum = data[0]
        for number in data:
            if number > maximum:
                maximum = number
        return maximum
if __name__ == '__main__':
    analyzer = NumberAnalyzer()
    list1 = [10, 5, 20, 8, 15]
    list2 = [-5, -1, -10, -3]
    list3 = [42]
    empty_list = []
    print(f"Maximum of {list1}: {analyzer.get_maximum(list1)}")
    print(f"Maximum of {list2}: {analyzer.get_maximum(list2)}")
    print(f"Maximum of {list3}: {analyzer.get_maximum(list3)}")
    try:
        analyzer.get_maximum(empty_list)
    except ValueError as e:
        print(f"Error for empty list: {e}")