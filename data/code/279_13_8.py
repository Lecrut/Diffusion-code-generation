class StringIterator:
    STRING_TO_ITERATE = 'Python'

    @staticmethod
    def print_chars():
        for char in StringIterator.STRING_TO_ITERATE:
            print(char)

if __name__ == '__main__':
    StringIterator.print_chars()