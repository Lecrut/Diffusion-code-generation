class NumberAppender:
    def __init__(self):
        self.numbers = []

    def append_numbers(self):
        for i in range(1, 6):
            self.numbers.append(i)

if __name__ == '__main__':
    appender = NumberAppender()
    appender.append_numbers()
    print(appender.numbers)