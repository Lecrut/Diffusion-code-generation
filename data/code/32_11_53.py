class CharacterCounter:
    def __init__(self, input_string):
        if not isinstance(input_string, str):
            raise ValueError("Input must be a string")
        self.input_string = input_string

    def get_character_count(self):
        return len(self.input_string)

if __name__ == '__main__':
    sample_input_1 = "Hello, World!"
    counter_1 = CharacterCounter(sample_input_1)
    print(counter_1.get_character_count())

    sample_input_2 = "Alibaba Cloud"
    counter_2 = CharacterCounter(sample_input_2)
    print(counter_2.get_character_count())