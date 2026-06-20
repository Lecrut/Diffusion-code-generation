class StringSorter:
    def sort_strings(self, strings):
        if not strings:
            return []
        
        def sort_key(s):
            return (len(s), s)
        
        sorted_strings = sorted(strings, key=sort_key)
        return sorted_strings

if __name__ == '__main__':
    sorter = StringSorter()
    sample_strings = [
        "apple", "banana", "cherry", "date", "elderberry"
    ]
    print("Original Strings:")
    print(sample_strings)
    print("Sorted Strings:")
    print(sorter.sort_strings(sample_strings))