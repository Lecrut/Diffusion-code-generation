class NumberAnalyzer:
    def get_maximum(self, data_list):
        if not data_list:
            raise ValueError("Input list cannot be empty")
        maximum = data_list[0]
        for number in data_list[1:]:
            if number > maximum:
                maximum = number
        return maximum
if __name__ == '__main__':
    analyzer = NumberAnalyzer()
    list1 = [10, 5, 20, 8, 15]
    list2 = [-5, -1, -10, -3]
    list3 = [42]
    list4 = []
    print(f"Maximum of {list1}: {analyzer.get_maximum(list1)}")
    print(f"Maximum of {list2}: {analyzer.get_maximum(list2)}")
    print(f"Maximum of {list3}: {analyzer.get_maximum(list3)}")
    try:
        analyzer.get_maximum(list4)
    except ValueError as e:
        print(f"Error for {list4}: {e}")