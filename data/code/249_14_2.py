class ListAnalyzer:
    def get_largest(self, data_list):
        if not data_list:
            raise ValueError("Input list cannot be empty")
        largest = data_list[0]
        for item in data_list[1:]:
            if item > largest:
                largest = item
        return largest
if __name__ == '__main__':
    analyzer = ListAnalyzer()
    sample_list_1 = [10, 5, 20, 8, 15]
    sample_list_2 = [-5, -1, -10, -3]
    sample_list_3 = [42]
    sample_list_4 = []
    print(f"Largest in {sample_list_1}: {analyzer.get_largest(sample_list_1)}")
    print(f"Largest in {sample_list_2}: {analyzer.get_largest(sample_list_2)}")
    print(f"Largest in {sample_list_3}: {analyzer.get_largest(sample_list_3)}")
    try:
        analyzer.get_largest(sample_list_4)
    except ValueError as e:
        print(f"Error for {sample_list_4}: {e}")