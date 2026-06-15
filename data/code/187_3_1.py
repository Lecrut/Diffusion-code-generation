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
    sample_list_one = [10, 5, 20, 8, 15]
    sample_list_two = [-5, -1, -10, -3]
    sample_list_three = [42]
    sample_list_empty = []
    result_one = analyzer.find_largest(sample_list_one)
    print(f"The largest value in {sample_list_one} is: {result_one}")
    result_two = analyzer.find_largest(sample_list_two)
    print(f"The largest value in {sample_list_two} is: {result_two}")
    result_three = analyzer.find_largest(sample_list_three)
    print(f"The largest value in {sample_list_three} is: {result_three}")
    try:
        analyzer.find_largest(sample_list_empty)
    except ValueError as e:
        print(f"Error for empty list: {e}")