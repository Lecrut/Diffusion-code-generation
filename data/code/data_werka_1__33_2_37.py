class SpaceRemover:
    def __init__(self, text):
        self.text = text

    def remove_spaces(self):
        return ''.join(self.text.split())

if __name__ == '__main__':
    sample_string = "  This is a sample string with   various spaces. \nIt has   multiple lines. "
    remover = SpaceRemover(sample_string)
    print(remover.remove_spaces())