class StringComparer:
    @staticmethod
    def compare(str1, str2):
        len_diff = abs(len(str1) - len(str2))
        is_strictly_greater = str1 > str2
        return (len_diff, is_strictly_greater)

if __name__ == '__main__':
    comparer = StringComparer()
    s1 = "apple"
    s2 = "banana"
    result1 = comparer.compare(s1, s2)
    print(f"Comparing '{s1}' and '{s2}': {result1}")
    
    s3 = "cherry"
    s4 = "date"
    result2 = comparer.compare(s3, s4)
    print(f"Comparing '{s3}' and '{s4}': {result2}")
    
    s5 = "elderberry"
    s6 = "elderberry"
    result3 = comparer.compare(s5, s6)
    print(f"Comparing '{s5}' and '{s6}': {result3}")