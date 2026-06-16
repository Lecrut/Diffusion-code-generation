class StringUtility:
    def calculate_length(self, s: str) -> int:
        return len(s)
if __name__ == '__main__':
    utility = StringUtility()
    test_string1 = "hello"
    test_string2 = ""
    test_string3 = "Python"
    print(f"Length of '{test_string1}': {utility.calculate_length(test_string1)}")
    print(f"Length of '{test_string2}': {utility.calculate_length(test_string2)}")
    print(f"Length of '{test_string3}': {utility.calculate_length(test_string3)}")