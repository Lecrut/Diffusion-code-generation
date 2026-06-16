class StringUtility:
    def calculate_length(self, s: str) -> int:
        return len(s)
if __name__ == '__main__':
    utility = StringUtility()
    sample_string1 = "hello"
    sample_string2 = ""
    sample_string3 = "Python"
    print(f"Length of '{sample_string1}': {utility.calculate_length(sample_string1)}")
    print(f"Length of '{sample_string2}': {utility.calculate_length(sample_string2)}")
    print(f"Length of '{sample_string3}': {utility.calculate_length(sample_string3)}")