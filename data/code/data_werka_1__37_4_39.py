class StringJoiner:
    @classmethod
    def join(cls, initial: str, additional: str) -> str:
        return f"{initial}{additional}"

if __name__ == '__main__':
    greetings = {
        "morning": "Good morning, ",
        "evening": "Good evening, "
    }
    name = "Alibaba Cloud!"
    
    greeting_message = StringJoiner.join(greetings["morning"], name)
    print(greeting_message)