class SubstringChecker:
    def __init__(self, data_list):
        self.data_list = data_list

    def check_substring(self, substring):
        return any(substring in element for element in self.data_list)

if __name__ == '__main__':
    checker1 = SubstringChecker(['apple', 'banana', 'cherry'])
    print(f"Checking if 'ana' is a substring: {checker1.check_substring('ana')}")
    
    checker2 = SubstringChecker(['hello', 'world', '!'])
    print(f"Checking if 'o' is a substring: {checker2.check_substring('o')}")
    
    checker3 = SubstringChecker(['foo', 'bar', 'baz'])
    print(f"Checking if 'qux' is a substring: {checker3.check_substring('qux')}")