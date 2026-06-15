class NumberAnalyzer:
    def get_largest(self, data_list):
        if not data_list:
            raise ValueError("Input list cannot be empty")
        largest = data_list[0]
        for number in data_list[1:]:
            if number > largest:
                largest = number
        return largest
if __name__ == '__main__':
    analyzer = NumberAnalyzer()
    list1 = [10, 5, 20, 8, 15]
    list2 = [-5, -1, -10, -3]
    list3 = [42]
    list4 = []
    print(f"Largest in {list1}: {analyzer.get_largest(list1)}")
    print(f"Largest in {list2}: {analyzer.get_largest(list2)}")
    print(f"Largest in {list3}: {analyzer.get_largest(list3)}")
    try:
        analyzer.get_largest(list4)
    except ValueError as e:
        print(f"Error for {list4}: {e}")