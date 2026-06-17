class NumberAnalyzer:
    def find_maximum(self, numbers):
        if not numbers:
            raise ValueError("Input list cannot be empty")
        maximum = numbers[0]
        for number in numbers[1:]:
            if number > maximum:
                maximum = number
        return maximum
if __name__ == '__main__':
    analyzer = NumberAnalyzer()
    list1 = [10, 5, 20, 8, 15]
    list2 = [-5, -1, -10, -3]
    list3 = [42]
    list4 = []
    print(f"Maximum in {list1}: {analyzer.find_maximum(list1)}")
    print(f"Maximum in {list2}: {analyzer.find_maximum(list2)}")
    print(f"Maximum in {list3}: {analyzer.find_maximum(list3)}")
    try:
        analyzer.find_maximum(list4)
    except ValueError as e:
        print(f"Error for {list4}: {e}")