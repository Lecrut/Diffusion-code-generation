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
    str1 = "apple"
    str2 = "banana"
    result_str = comparator.compare_lengths(str1, str2)
    print(f"Comparing '{str1}' and '{str2}': {result_str}")
    str3 = "short"
    str4 = "longerstring"
    result_str2 = comparator.compare_lengths(str3, str4)
    print(f"Comparing '{str3}' and '{str4}': {result_str2}")
    list1 = [1, 2, 3]
    list2 = [4, 5]
    result_list = comparator.compare_lengths(list1, list2)
    print(f"Comparing {list1} and {list2}: {result_list}")
    list3 = ['a', 'b', 'c']
    list4 = ['x', 'y', 'z']
    result_list2 = comparator.compare_lengths(list3, list4)
    print(f"Comparing {list3} and {list4}: {result_list2}")
    list5 = []
    list6 = [10]
    result_list3 = comparator.compare_lengths(list5, list6)
    print(f"Comparing {list5} and {list6}: {result_list3}")