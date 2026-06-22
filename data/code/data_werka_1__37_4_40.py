class StringCombiner:
    @classmethod
    def combine_strings(cls, first_string: str, second_string: str) -> str:
        return f"{first_string}{second_string}"

if __name__ == '__main__':
    result = StringCombiner.combine_strings("Hello, ", "World!")
    print(result)