class StringComparer:
    def compare(self, str1, str2):
        len_diff = abs(len(str1) - len(str2))
        alpha_diff = self._compare_alphabetically(str1, str2)
        is_strictly_greater = (len_diff == 0 and alpha_diff > 0) or len_diff < 0
        return (len_diff, alpha_diff, is_strictly_greater)

    @staticmethod
    def _compare_alphabetically(s1, s2):
        min_length = min(len(s1), len(s2))
        for i in range(min_length):
            if s1[i] > s2[i]:
                return 1
            elif s1[i] < s2[i]:
                return -1
        return len(s1) - len(s2)

if __name__ == '__main__':
    comparer = StringComparer()
    strA = "apple"
    strB = "banana"
    result1 = comparer.compare(strA, strB)
    print(f"Comparing '{strA}' and '{strB}': {result1}")
    
    strC = "cherry"
    strD = "date"
    result2 = comparer.compare(strC, strD)
    print(f"Comparing '{strC}' and '{strD}': {result2}")
    
    strE = "elderberry"
    strF = "elderberry"
    result3 = comparer.compare(strE, strF)
    print(f"Comparing '{strE}' and '{strF}': {result3}")