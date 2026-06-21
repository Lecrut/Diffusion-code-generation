class LengthValidator:
    def __init__(self, length1, length2):
        self.lengths = {'length1': length1, 'length2': length2}

    def validate_lengths(self):
        for key, value in self.lengths.items():
            if value < 0:
                raise ValueError(f"{key} cannot be negative")

    def compare_lengths(self):
        self.validate_lengths()
        return abs(self.lengths['length1'] - self.lengths['length2'])

if __name__ == '__main__':
    validator = LengthValidator(7, 3)
    try:
        difference = validator.compare_lengths()
        print(difference)
    except ValueError as e:
        print(e)