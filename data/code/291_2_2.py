class LengthComparator:
    def compare_lengths(self, seq1, seq2):
        return len(seq1) - len(seq2)
if __name__ == '__main__':
    comparator = LengthComparator()
    string1 = "hello"
    string2 = "world"
    list1 = [1, 2, 3]
    list2 = ['a', 'b', 'c']
    print(f"Length difference between '{string1}' and '{string2}': {comparator.compare_lengths(string1, string2)}")
    print(f"Length difference between list {list1} and list {list2}: {comparator.compare_lengths(list1, list2)}")