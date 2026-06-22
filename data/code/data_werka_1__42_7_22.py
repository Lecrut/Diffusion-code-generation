class StringJoiner:
    def __init__(self, list_of_strings, delimiter):
        if not isinstance(list_of_strings, list) or not all(isinstance(s, str) for s in list_of_strings):
            raise ValueError("list_of_strings must be a list of strings")
        if not isinstance(delimiter, str):
            raise ValueError("delimiter must be a string")
        self.list_of_strings = list_of_strings
        self.delimiter = delimiter

    def join(self):
        return self.delimiter.join(self.list_of_strings)

if __name__ == '__main__':
    try:
        sample_list = ["apple", "banana", "cherry", "date"]
        custom_delimiter = " | "
        string_joiner = StringJoiner(sample_list, custom_delimiter)
        result = string_joiner.join()
        print(result)
    except ValueError as e:
        print(e)