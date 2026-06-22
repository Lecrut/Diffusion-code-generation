class StringJoiner:
    @classmethod
    def join_strings(cls, initial: str, addition: str) -> str:
        return f"{initial}{addition}"

if __name__ == '__main__':
    instance = StringJoiner()
    
    first = "Good evening, "
    second = "Qwen!"
    result_one = instance.join_strings(first, second)
    print(result_one)
    
    third = "Welcome to Alibaba Cloud, "
    fourth = "Innovate with us."
    result_two = instance.join_strings(third, fourth)
    print(result_two)