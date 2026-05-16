class SequenceAnalyzer:
    @staticmethod
    def get_middle(data):
        n = len(data)
        if n == 0:
            raise ValueError("Input list cannot be empty")
        middle_index = n // 2
        return data[middle_index]
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, 20, 30]
    list3 = [7]
    list4 = []
    print(f"Middle of {list1}: {SequenceAnalyzer.get_middle(list1)}")
    print(f"Middle of {list2}: {SequenceAnalyzer.get_middle(list2)}")
    print(f"Middle of {list3}: {SequenceAnalyzer.get_middle(list3)}")
    try:
        SequenceAnalyzer.get_middle(list4)
    except ValueError as e:
        print(f"Error for {list4}: {e}")