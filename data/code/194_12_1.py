class StringAnalyzer:
    @staticmethod
    def find_longest_string(string_list):
        if not string_list:
            return None
        longest_string = ""
        for s in string_list:
            if len(s) > len(longest_string):
                longest_string = s
        return longest_string
if __name__ == '__main__':
    data1 = ["apple", "banana", "kiwi", "strawberry", "grape"]
    result1 = StringAnalyzer.find_longest_string(data1)
    print(f"Data: {data1}")
    print(f"Longest string: {result1}")
    data2 = ["short", "longer", "longest", "a", "test"]
    result2 = StringAnalyzer.find_longest_string(data2)
    print(f"Data: {data2}")
    print(f"Longest string: {result2}")
    data3 = []
    result3 = StringAnalyzer.find_longest_string(data3)
    print(f"Data: {data3}")
    print(f"Longest string: {result3}")
    data4 = ["hello", "world"]
    result4 = StringAnalyzer.find_longest_string(data4)
    print(f"Data: {data4}")
    print(f"Longest string: {result4}")