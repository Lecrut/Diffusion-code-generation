class StringCombiner:
    @classmethod
    def combine_strings(cls, first: str, second: str) -> str:
        return f"{first}{second}"

if __name__ == '__main__':
    result = StringCombiner.combine_strings("Hello, ", "World!")
    print(result)