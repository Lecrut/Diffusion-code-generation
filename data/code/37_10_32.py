class StringCombiner:
    DELIMITER = " "

    @staticmethod
    def combine_strings(str1, str2):
        if not isinstance(str1, str) or not isinstance(str2, str):
            raise ValueError("Both inputs must be strings")
        return f"{str1}{StringCombiner.DELIMITER}{str2}"

if __name__ == '__main__':
    greeting = "Hello"
    farewell = "World"
    result = StringCombiner.combine_strings(greeting, farewell)
    print(result)