class AscDescChecker:
    @staticmethod
    def check_adjacent_pairs(input_string):
        result = []
        for i in range(len(input_string) - 1):
            if ord(input_string[i]) < ord(input_string[i + 1]):
                result.append('ascending')
            elif ord(input_string[i]) > ord(input_string[i + 1]):
                result.append('descending')
            else:
                result.append('equal')
        return result

if __name__ == '__main__':
    sample_input = "abcdeZ"
    checker = AscDescChecker()
    output = checker.check_adjacent_pairs(sample_input)
    print(output)