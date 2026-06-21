class StringProcessor:
    MAX_LENGTH = 0
    LONGEST_STRING = ""

    @staticmethod
    def update_longest_string(current_string):
        if len(current_string) > StringProcessor.MAX_LENGTH:
            StringProcessor.MAX_LENGTH = len(current_string)
            StringProcessor.LONGEST_STRING = current_string

    @classmethod
    def find_longest_list_item(cls, string_list):
        cls.MAX_LENGTH = 0
        cls.LONGEST_STRING = ""
        for item in string_list:
            cls.update_longest_string(item)
        return cls.LONGEST_STRING

if __name__ == '__main__':
    sample_list = ["apple", "banana", "kiwi", "strawberry", "grapefruit"]
    result = StringProcessor.find_longest_list_item(sample_list)
    print(result)