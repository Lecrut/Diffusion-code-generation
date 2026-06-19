class StringCombiner:
    SEPARATOR = " "

    @staticmethod
    def combine_strings(str1, str2):
        if not isinstance(str1, str) or not isinstance(str2, str):
            raise ValueError("Both inputs must be strings")
        return f"{str1}{StringCombiner.SEPARATOR}{str2}"

if __name__ == '__main__':
    sample_values = [
        ("Hello", "World"),
        ("Goodbye", "Everyone"),
        ("Python", "Programming")
    ]
    for s1, s2 in sample_values:
        try:
            result = StringCombiner.combine_strings(s1, s2)
            print(result)
        except ValueError as e:
            print(e)