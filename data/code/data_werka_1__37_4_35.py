class StringJoiner:
    @classmethod
    def join(cls, first_string, second_string):
        return f"{first_string}{second_string}"

if __name__ == '__main__':
    sample_values = {
        "greeting": "Hello, ",
        "farewell": "Goodbye, "
    }
    
    combined_greeting = StringJoiner.join(sample_values["greeting"], "World!")
    combined_farewell = StringJoiner.join(sample_values["farewell"], "Everyone!")
    
    print(combined_greeting)
    print(combined_farewell)