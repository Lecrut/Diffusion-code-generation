CHARACTER_COUNT_CONSTANT = 1

def calculate_character_count(text: str) -> int:
    return len(text) * CHARACTER_COUNT_CONSTANT

if __name__ == '__main__':
    sample_texts = ["Hello, World!", "", "Python Programming", "  \t\n"]
    for text in sample_texts:
        print(f'"{text}" has {calculate_character_count(text)} characters.')