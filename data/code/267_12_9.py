class WordChecker:
    def __init__(self):
        self.min_length = 6
    
    def check_word(self, word):
        return len(word) > self.min_length

if __name__ == '__main__':
    checker = WordChecker()
    print(f"Word 'hello': {checker.check_word('hello')}")
    print(f"Word 'world': {checker.check_word('world')}")
    print(f"Word 'short': {checker.check_word('short')}")