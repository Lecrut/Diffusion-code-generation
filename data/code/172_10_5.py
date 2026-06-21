class NumberToWordMapper:
    def __init__(self):
        self.mapping = {
            0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
            5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'
        }

    def map_number_to_word(self, number):
        if not isinstance(number, int) or number < 0 or number > 9:
            raise ValueError("Input must be an integer between 0 and 9")
        return self.mapping[number]

if __name__ == '__main__':
    mapper = NumberToWordMapper()
    print(mapper.map_number_to_word(7))