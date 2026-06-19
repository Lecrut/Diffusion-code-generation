class StringJoiner:
    @classmethod
    def join(cls, initial: str, additional: str) -> str:
        if not isinstance(initial, str) or not isinstance(additional, str):
            raise ValueError("Both parameters must be strings.")
        return f"{initial}{additional}"

if __name__ == '__main__':
    try:
        first_half = "Greetings, "
        second_half = "Earthlings!"
        full_greeting = StringJoiner.join(first_half, second_half)
        print(full_greeting)
    except ValueError as e:
        print(e)