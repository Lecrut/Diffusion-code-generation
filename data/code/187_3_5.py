class ListAnalyzer:
    def find_largest(self, data):
        if not data:
            raise ValueError("Input list cannot be empty")
        largest = data[0]
        for item in data:
            if item > largest:
                largest = item
        return largest
if __name__ == '__main__':
    analyzer = ListAnalyzer()
    sample_list1 = [10, 5, 20, 8, 15]
    sample_list2 = [-5, -1, -10, -3]
    sample_list3 = [42]
    sample_list4 = []
    print(f"Largest in {sample_list1}: {analyzer.find_largest(sample_list1)}")
    print(f"Largest in {sample_list2}: {analyzer.find_largest(sample_list2)}")
    print(f"Largest in {sample_list3}: {analyzer.find_largest(sample_list3)}")
    try:
        analyzer.find_largest(sample_list4)
    except ValueError as e:
        print(f"Error for {sample_list4}: {e}")