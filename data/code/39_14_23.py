class SubstringGenerator:

    def __init__(self, s):
        if not isinstance(s, str):
            raise ValueError('Input must be a string')
        self.s = s
        self.length = len(s)

    def generate(self):
        for start in range(self.length):
            for end in range(start + 1, self.length + 1):
                yield self.s[start:end]
if __name__ == '__main__':
    input_string = 'abc'
    try:
        generator = SubstringGenerator(input_string)
        all_substrings = list(generator.generate())
        print(all_substrings)
    except ValueError as e:
        print(e)
    test_string_2 = 'a'
    try:
        generator_2 = SubstringGenerator(test_string_2)
        result_list_2 = list(generator_2.generate())
        print(result_list_2)
    except ValueError as e:
        print(e)
    test_string_3 = 'ab'
    try:
        generator_3 = SubstringGenerator(test_string_3)
        result_list_3 = list(generator_3.generate())
        print(result_list_3)
    except ValueError as e:
        print(e)