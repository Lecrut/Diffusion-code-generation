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
    sample_list_1 = [10, 5, 20, 8, 15]
    sample_list_2 = [-5, -1, -10, -3]
    sample_list_3 = [42]
    sample_list_4 = []
    result_1 = analyzer.find_largest(sample_list_1)
    print(f"The largest value in {sample_list_1} is: {result_1}")
    result_2 = analyzer.find_largest(sample_list_2)
    print(f"The largest value in {sample_list_2} is: {result_2}")
    result_3 = analyzer.find_largest(sample_list_3)
    print(f"The largest value in {sample_list_3} is: {result_3}")
    try:
        analyzer.find_largest(sample_list_4)
    except ValueError as e:
        print(f"Error for {sample_list_4}: {e}")