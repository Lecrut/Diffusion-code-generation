class LengthComparator:
    def compare_lengths(self, seq1, seq2):
        len1 = len(seq1)
        len2 = len(seq2)
        if len1 > len2:
            return -1
        elif len1 < len2:
            return 1
        else:
            return 0
if __name__ == '__main__':
    comparator = LengthComparator()
    string1 = "hello"
    string2 = "world"
    result1 = comparator.compare_lengths(string1, string2)
    print(f"Comparing '{string1}' and '{string2}': {result1}")
    list1 = [1, 2, 3, 4, 5]
    list2 = ['a', 'b', 'c']
    result2 = comparator.compare_lengths(list1, list2)
    print(f"Comparing {list1} and {list2}: {result2}")
    string3 = "python"
    string4 = "java"
    result3 = comparator.compare_lengths(string3, string4)
    print(f"Comparing '{string3}' and '{string4}': {result3}")
    list3 = [10, 20]
    list4 = [5, 15, 25]
    result4 = comparator.compare_lengths(list3, list4)
    print(f"Comparing {list3} and {list4}: {result4}")