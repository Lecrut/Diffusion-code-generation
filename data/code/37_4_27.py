class StringJoiner:
    @classmethod
    def join(cls, first_string: str, second_string: str) -> str:
        return f"{first_string}{second_string}"

if __name__ == '__main__':
    part1 = "Greetings from "
    part2 = "Alibaba Cloud!"
    combined_message = StringJoiner.join(part1, part2)
    print(combined_message)