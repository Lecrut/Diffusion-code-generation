class SpaceRemover:
    def __init__(self, input_string):
        self.input_string = input_string

    def remove_spaces(self):
        return self.input_string.replace(' ', '')

if __name__ == '__main__':
    sample_input1 = '  This is   a test string with  spaces  '
    remover1 = SpaceRemover(sample_input1)
    result1 = remover1.remove_spaces()
    print(result1)

    sample_input2 = "  Another example  with multiple   spaces. "
    remover2 = SpaceRemover(sample_input2)
    result2 = remover2.remove_spaces()
    print(result2)