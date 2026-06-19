class StringJoiner:
    @classmethod
    def join_strings(cls, initial: str, additional: str) -> str:
        return f"{initial}{additional}"

if __name__ == '__main__':
    SALUTATION = "Greetings, "
    NAME = "Qwen"
    combined_greeting = StringJoiner.join_strings(SALUTATION, NAME)
    print(combined_greeting)