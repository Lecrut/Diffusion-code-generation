class SpaceRemover:
    def __init__(self, input_string):
        self.input_string = input_string

    def remove_spaces(self):
        return self.input_string.replace(" ", "").replace("\t", "").replace("\n", "")

if __name__ == '__main__':
    sample_input = "This is a \tsample string.\nIt contains spaces, tabs,\tand newlines."
    remover = SpaceRemover(sample_input)
    result = remover.remove_spaces()
    print(result)