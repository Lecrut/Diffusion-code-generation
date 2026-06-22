class Repeater:
    def repeat(self, s: str, n: int) -> str:
        return s * n

if __name__ == '__main__':
    repeater = Repeater()
    result1 = repeater.repeat("abc", 5)
    print(f"'abc' repeated 5 times is: '{result1}'")
    result2 = repeater.repeat("hello", 3)
    print(f"'hello' repeated 3 times is: '{result2}'")
    result3 = repeater.repeat("Python", 1)
    print(f"'Python' repeated 1 time is: '{result3}'")