class StringProcessor:
    MAX_LENGTH = 0

    @staticmethod
    def initialize_max_length():
        StringProcessor.MAX_LENGTH = 0

    @staticmethod
    def update_max_length(current_string):
        if len(current_string) > StringProcessor.MAX_LENGTH:
            StringProcessor.MAX_LENGTH = len(current_string)

    @staticmethod
    def find_longest_list_item(string_list):
        StringProcessor.initialize_max_length()
        for s in string_list:
            StringProcessor.update_max_length(s)
        return StringProcessor.MAX_LENGTH

if __name__ == '__main__':
    sample_list = ["apple", "banana", "kiwi", "strawberry", "grapefruit"]
    result = StringProcessor.find_longest_list_item(sample_list)
    print(result)