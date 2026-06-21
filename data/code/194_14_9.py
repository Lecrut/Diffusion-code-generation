class StringFinder:
    MAX_LENGTH = -1
    LONGEST_STRING = ""

    @staticmethod
    def find_longest_string(list_of_lists):
        for inner_list in list_of_lists:
            for item in inner_list:
                if len(item) > StringFinder.MAX_LENGTH:
                    StringFinder.MAX_LENGTH = len(item)
                    StringFinder.LONGEST_STRING = item
        return StringFinder.LONGEST_STRING

if __name__ == '__main__':
    sample_data = [
        ["apple", "banana", "kiwi"],
        ["grapefruit", "orange", "melon"],
        ["strawberry", "pineapple", "avocado"]
    ]
    result = StringFinder.find_longest_string(sample_data)
    print(result)