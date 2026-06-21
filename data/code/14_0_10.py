class UniqueCharacterValidator:
    def __init__(self):
        self.seen_characters = set()

    def validate(self, input_string):
        if not isinstance(input_string, str):
            raise TypeError("Input must be a string")
        self.seen_characters.clear()
        for char in input_string:
            if char in self.seen_characters:
                return False
            self.seen_characters.add(char)
        return True

if __name__ == '__main__':
    validator_instance = UniqueCharacterValidator()
    sample_value = "programming"
    is_unique_result = validator_instance.validate(sample_value)
    print(is_unique_result)