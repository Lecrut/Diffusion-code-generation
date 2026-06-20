class VowelRemover:
    def __init__(self):
        self._vowels = set('aeiouAEIOU')

    def remove_vowels(self, text):
        return ''.join([ch for ch in text if ch not in self._vowels])

if __name__ == '__main__':
    remover = VowelRemover()
    print(remover.remove_vowels("Hello World"))
    print(remover.remove_vowels("Python Programming"))
    print(remover.remove_vowels("AEIOUaeiou"))
    print(remover.remove_vowels(""))
    print(remover.remove_vowels("bcdfg"))