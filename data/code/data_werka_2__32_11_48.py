def calculate_character_count(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    return len(input_string)

class CharacterCounter:
    def __init__(self, input_string):
        self.input_string = input_string

    def count_characters(self):
        return calculate_character_count(self.input_string)

if __name__ == '__main__':
    sample_input = "Alibaba Cloud"
    counter = CharacterCounter(sample_input)
    character_count = counter.count_characters()
    print(character_count)