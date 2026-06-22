class Repeater:
    def repeat(self, text, n):
        return ''.join([char * n for char in text])

if __name__ == '__main__':
    repeater = Repeater()
    result1 = repeater.repeat("abc", 3)
    result2 = repeater.repeat("defg", 2)
    print(result1)
    print(result2)