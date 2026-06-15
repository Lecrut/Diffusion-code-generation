class NumberAnalyzer:
    def find_maximum(self, numbers):
        if not numbers:
            raise ValueError("Input list cannot be empty")
        maximum = numbers[0]
        for number in numbers:
            if number > maximum:
                maximum = number
        return maximum
if __name__ == '__main__':
    analyzer = NumberAnalyzer()
    sample_list1 = [10, 5, 22, 8, 30]
    sample_list2 = [-5, -1, -100, -2]
    sample_list3 = [7]
    sample_list4 = []
    print(f"Maximum of {sample_list1}: {analyzer.find_maximum(sample_list1)}")
    print(f"Maximum of {sample_list2}: {analyzer.find_maximum(sample_list2)}")
    print(f"Maximum of {sample_list3}: {analyzer.find_maximum(sample_list3)}")
    try:
        analyzer.find_maximum(sample_list4)
    except ValueError as e:
        print(f"Error for {sample_list4}: {e}")