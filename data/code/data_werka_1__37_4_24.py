class StringConcatenator:
    @classmethod
    def concatenate(cls, prefix: str, suffix: str) -> str:
        return f"{prefix}{suffix}"

if __name__ == '__main__':
    greeting = "Hi there, "
    name = "Qwen!"
    full_message = StringConcatenator.concatenate(greeting, name)
    print(full_message)