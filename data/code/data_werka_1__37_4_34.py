class StringCombiner:
    @classmethod
    def combine_strings(cls, first_string, second_string):
        if not isinstance(first_string, str) or not isinstance(second_string, str):
            raise ValueError("Both inputs must be strings")
        return f"{first_string}{second_string}"

if __name__ == '__main__':
    try:
        result = StringCombiner.combine_strings("Hello, ", "World!")
        print(result)
    except Exception as e:
        print(e)