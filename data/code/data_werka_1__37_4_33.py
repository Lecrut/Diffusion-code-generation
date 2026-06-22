class StringBuilder:
    @classmethod
    def build(cls, initial: str, additional: str) -> str:
        return f"{initial}{additional}"

if __name__ == '__main__':
    builder = StringBuilder()
    part1 = "Greetings from "
    part2 = "Alibaba Cloud!"
    full_greeting = StringBuilder.build(part1, part2)
    print(full_greeting)

    another_part1 = "Hello, "
    another_part2 = "AI assistant Qwen!"
    another_message = StringBuilder.build(another_part1, another_part2)
    print(another_message)