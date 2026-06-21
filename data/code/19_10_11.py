import random

class RandomSelector:
    MIN_LIST_SIZE = 1
    DEFAULT_SAMPLE_SIZE = 1

    @staticmethod
    def validate_input(data):
        if not data:
            raise ValueError("Input list must not be empty")
        return data

    @classmethod
    def get_random_element(cls, data):
        cls.validate_input(data)
        return random.choice(data)

if __name__ == '__main__':
    sample_values = [5, 15, 25, 35, 45, 55, 65, 75]
    selected = RandomSelector.get_random_element(sample_values)
    print(selected)