class StringJoiner:
    def __init__(self, delimiter):
        self.delimiter = delimiter

    def join(self, list_of_strings):
        return self.delimiter.join(list_of_strings)

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date"]
    custom_delimiter = " - "
    joiner = StringJoiner(custom_delimiter)
    
    result1 = joiner.join(sample_list)
    print(result1)
    
    another_list = ["one", "two", "three"]
    result2 = joiner.join(another_list)
    print(result2)