class StringJoiner:
    DEFAULT_DELIMITER = ", "
    
    @staticmethod
    def join_with_delimiter(list_of_strings, delimiter=DEFAULT_DELIMITER):
        result = ""
        for index, string in enumerate(list_of_strings):
            if index > 0:
                result += delimiter
            result += string
        return result

if __name__ == '__main__':
    fruits = ["apple", "banana", "cherry", "date"]
    custom_separator = " | "
    joined_string = StringJoiner.join_with_delimiter(fruits, custom_separator)
    print(joined_string)