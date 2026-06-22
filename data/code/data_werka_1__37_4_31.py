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
    time_of_day = "morning"
    
    full_greeting = StringJoiner.join(greetings[time_of_day], name)
    print(full_greeting)