class ListAnalyzer:
    def find_largest(self, data):
        if not data:
            raise ValueError("Input list cannot be empty")
        largest = data[0]
        for item in data[1:]:
            if item > largest:
                largest = item
        return largest
if __name__ == '__main__':
    analyzer = ListAnalyzer()
    sample_list1 = [10, 5, 20, 8, 15]
    sample_list2 = [-5, -1, -10, -3]
    sample_list3 = [42]
    sample_list4 = []
    result1 = analyzer.find_largest(sample_list1)
    print(f"The largest value in {sample_list1} is: {result1}")
    result2 = analyzer.find_largest(sample_list2)
    print(f"The largest value in {sample_list2} is: {result2}")
    result3 = analyzer.find_largest(sample_list3)
    print(f"The largest value in {sample_list3} is: {result3}")
    try:
        analyzer.find_largest(sample_list4)
    except ValueError as e:
        print(f"Error for {sample_list4}: {e}")