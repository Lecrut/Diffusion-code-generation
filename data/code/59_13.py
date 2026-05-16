class SequenceAnalyzer:
    @staticmethod
    def get_middle(data):
        n = len(data)
        if n == 0:
            raise ValueError("Input list cannot be empty")
        middle_index = n // 2
        return data[middle_index]
if __name__ == '__main__':
    sample_list_odd = [1, 2, 3, 4, 5]
    sample_list_even = [10, 20, 30, 40]
    sample_list_single = [99]
    sample_list_empty = []
    print(f"Middle of {sample_list_odd}: {SequenceAnalyzer.get_middle(sample_list_odd)}")
    print(f"Middle of {sample_list_even}: {SequenceAnalyzer.get_middle(sample_list_even)}")
    print(f"Middle of {sample_list_single}: {SequenceAnalyzer.get_middle(sample_list_single)}")
    try:
        SequenceAnalyzer.get_middle(sample_list_empty)
    except ValueError as e:
        print(f"Error for empty list: {e}")