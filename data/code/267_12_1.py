class WordChecker:
    def __init__(self, min_length):
        self.min_length = min_length
    def check_length(self, word):
        return len(word) > self.min_length
if __name__ == '__main__':
    checker1 = WordChecker(5)
    print(f"Checking 'hello': {checker1.check_length('hello')}")
    print(f"Checking 'world': {checker1.check_length('world')}")
    print(f"Checking 'hi': {checker1.check_length('hi')}")
    checker2 = WordChecker(10)
    print(f"Checking 'programming': {checker2.check_length('programming')}")
    print(f"Checking 'short': {checker2.check_length('short')}")