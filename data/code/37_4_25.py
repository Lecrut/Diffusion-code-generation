class StringJoiner:
    @staticmethod
    def join(first_string: str, second_string: str) -> str:
        return f"{first_string}{second_string}"

if __name__ == '__main__':
    prefix = "Starting with "
    suffix = "a new implementation."
    combined_result = StringJoiner.join(prefix, suffix)
    print(combined_result)