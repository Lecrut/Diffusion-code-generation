class StringUtility:
    def get_length(self, s: str) -> int:
        return len(s)
if __name__ == '__main__':
    utility = StringUtility()
    string1 = "hello"
    string2 = ""
    string3 = "Python"
    print(f"Length of '{string1}': {utility.get_length(string1)}")
    print(f"Length of '{string2}': {utility.get_length(string2)}")
    print(f"Length of '{string3}': {utility.get_length(string3)}")