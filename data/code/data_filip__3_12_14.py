class VowelRemover:
    VOWELS = 'aeiouAEIOU'
    def __init__(self):
        self.table = str.maketrans('', '', self.VOWELS)
    def strip(self, text):
        return text.translate(self.table)

if __name__ == '__main__':
    remover = VowelRemover()
    print(remover.strip("Hello World"))
    print(remover.strip("AEIOUaeiou"))
    print(remover.strip("Python Programming"))