class StringCombiner:
    @classmethod
    def combine(cls, first: str, second: str) -> str:
        return f"{first}{second}"

if __name__ == '__main__':
    result = StringCombiner.combine("Hello, ", "World!")
    print(result)