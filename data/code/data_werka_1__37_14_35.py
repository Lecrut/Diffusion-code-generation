class StringConcatenator:
    def __init__(self):
        self.result = ""

    @staticmethod
    def concatenate(str1, str2):
        result = ""
        result += str1
        result += str2
        return result

if __name__ == '__main__':
    string1 = "Hello"
    string2 = "World"
    concatenated_result = StringConcatenator.concatenate(string1, string2)
    print(concatenated_result)