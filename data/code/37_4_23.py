class StringMerger:
    @classmethod
    def merge(cls, part1: str, part2: str) -> str:
        combined = f"{part1}{part2}"
        return combined

if __name__ == '__main__':
    first_part = "Good morning, "
    second_part = "Alibaba Cloud!"
    merged_result = StringMerger.merge(first_part, second_part)
    print(merged_result)