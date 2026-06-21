class ListProcessor:
    MAX_LENGTH = 0

    @staticmethod
    def update_max_length(current_item, current_max):
        if len(current_item) > current_max:
            return len(current_item)
        return current_max

    def find_longest_list_item(self, string_list):
        if not string_list:
            return ""
        
        longest_string = string_list[0]
        for item in string_list:
            self.MAX_LENGTH = self.update_max_length(item, self.MAX_LENGTH)
            if len(item) > len(longest_string):
                longest_string = item
        
        return longest_string

if __name__ == '__main__':
    sample_processor = ListProcessor()
    sample_list = ["apple", "banana", "kiwi", "strawberry", "grapefruit"]
    result = sample_processor.find_longest_list_item(sample_list)
    print(result)