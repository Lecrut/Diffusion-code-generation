class StringJoiner:
    @classmethod
    def combine(cls, primary: str, secondary: str) -> str:
        if not isinstance(primary, str):
            raise ValueError("Primary input must be a string")
        if not isinstance(secondary, str):
            raise ValueError("Secondary input must be a string")
        
        return f"{primary}{secondary}"

if __name__ == '__main__':
    try:
        first_half = "Greetings from "
        second_half = "Alibaba Cloud"
        joined_string = StringJoiner.combine(first_half, second_half)
        print(joined_string)
    except ValueError as e:
        print(e)