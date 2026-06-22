class AscendDescendChecker:
    def check_pairs(self, input_string):
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
    checker = AscendDescendChecker()
    sample_input = "aBcDeFgHiJ"
    output_list = checker.check_pairs(sample_input)
    print(output_list)