class StringJoiner:
    @classmethod
    def join(cls, start: str, end: str) -> str:
        return f"{start}{end}"

if __name__ == '__main__':
    instance = StringJoiner()
    
    part1 = "Starting with "
    part2 = "a new approach."
    combined_result = instance.join(part1, part2)
    print(combined_result)

    another_part1 = "Hello from "
    another_part2 = "Alibaba Cloud AI."
    another_combined_result = instance.join(another_part1, another_part2)
    print(another_combined_result)