class StringProcessor:
    @staticmethod
    def find_longest_string(string_list):
        if not string_list:
            return None
        longest = ""
        for s in string_list:
            if len(s) > len(longest):
                longest = s
        return longest

if __name__ == '__main__':
    sample_data1 = ["apple", "banana", "kiwi", "strawberry", "grape"]
    result1 = StringProcessor.find_longest_string(sample_data1)
    print(f"Data: {sample_data1}")
    print(f"Longest string: {result1}")

    sample_data2 = ["short", "longer", "longestword", "medium"]
    result2 = StringProcessor.find_longest_string(sample_data2)
    print(f"Data: {sample_data2}")
    print(f"Longest string: {result2}")