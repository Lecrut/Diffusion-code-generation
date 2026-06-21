CHARACTER_COUNT_MAP = {
    "Hello, World!": 13,
    "Python": 6,
    "": 0,
    "OpenAI": 6,
    "ChatGPT": 7
}

def calculate_character_count(input_string):
    return len(input_string)

if __name__ == '__main__':
    sample_input = "Hello, World!"
    character_count = calculate_character_count(sample_input)
    print(character_count)