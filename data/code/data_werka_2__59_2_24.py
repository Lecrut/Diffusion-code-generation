class SequenceAnalyzer:
    def get_middle(self, iterable):
        if not iterable:
            raise ValueError("The iterable is empty")
        sorted_iterable = sorted(iterable)
        length = len(sorted_iterable)
        mid_index = length // 2
        if length % 2 == 0:
            return (sorted_iterable[mid_index - 1] + sorted_iterable[mid_index]) / 2
        else:
            return sorted_iterable[mid_index]

if __name__ == '__main__':
    analyzer = SequenceAnalyzer()
    sample_list1 = [3, 1, 4, 1, 5, 9, 2]
    sample_tuple = (8, 6, 7, 5, 3, 0, 9)
    sample_string = "hello"
    
    print("Median of sample_list1:", analyzer.get_middle(sample_list1))
    print("Median of sample_tuple:", analyzer.get_middle(sample_tuple))
    print("Median of sample_string:", analyzer.get_middle(sample_string))