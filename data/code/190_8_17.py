class SubstringChecker:
    def __init__(self, data_list):
        self.data_list = data_list

    def contains_substring(self, item):
        return any(item in element for element in self.data_list)

if __name__ == '__main__':
    checker1 = SubstringChecker(['apple', 'banana', 'cherry'])
    print(f"Checking if 'an' is in ['apple', 'banana', 'cherry']: {checker1.contains_substring('an')}")
    checker2 = SubstringChecker(['hello', 'world'])
    print(f"Checking if 'bye' is in ['hello', 'world']: {checker2.contains_substring('bye')}")