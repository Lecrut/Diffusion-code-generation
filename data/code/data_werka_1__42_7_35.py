class StringJoiner:
    def __init__(self, list_of_strings):
        self.list_of_strings = list_of_strings

    def join_with_delimiter(self, delimiter):
        return delimiter.join(self.list_of_strings)

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date"]
    custom_delimiter = " | "
    
    joiner_instance = StringJoiner(sample_list)
    result1 = joiner_instance.join_with_delimiter(custom_delimiter)
    print(result1)
    
    another_delimiter = "; "
    result2 = joiner_instance.join_with_delimiter(another_delimiter)
    print(result2)