class StringJoiner:
    def __init__(self):
        self.prefix = ""
    
    def set_prefix(self, prefix):
        self.prefix = prefix
    
    def join_strings(self, str1, str2):
        return ''.join([self.prefix, str1, str2])

if __name__ == '__main__':
    joiner = StringJoiner()
    joiner.set_prefix("Hello")
    string1 = ", "
    string2 = "World!"
    combined_result = joiner.join_strings(string1, string2)
    print(combined_result)