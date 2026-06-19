class StringJoiner:
    def __init__(self, list_of_strings, delimiter):
        self.list_of_strings = list_of_strings
        self.delimiter = delimiter

    def join(self):
        return self.delimiter.join(self.list_of_strings)

if __name__ == '__main__':
    fruits = ["apple", "banana", "cherry", "date"]
    separator = "; "
    
    joiner = StringJoiner(fruits, separator)
    result = joiner.join()
    print(result)