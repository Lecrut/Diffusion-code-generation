class WordChecker:
    def __init__(self, min_length):
        self.min_length = min_length
    def check_length(self, word):
        return len(word) > self.min_length
if __name__ == '__main__':
    checker1 = WordChecker(5)
    print(f"Word 'hello': {checker1.check_length('hello')}")
    print(f"Word 'world': {checker1.check_length('world')}")
    print(f"Word 'hi': {checker1.check_length('hi')}")
    checker2 = WordChecker(3)
    print(f"Word 'testing': {checker2.check_length('testing')}")
    print(f"Word 'a': {checker2.check_length('a')}")