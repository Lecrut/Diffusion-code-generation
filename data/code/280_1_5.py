class NumberAppender:
    def __init__(self):
        self.numbers = []

    def append_numbers(self):
        for i in range(1, 6):
            self.numbers.append(i)

    def get_numbers(self):
        return self.numbers

if __name__ == '__main__':
    appender = NumberAppender()
    appender.append_numbers()
    result = appender.get_numbers()
    print(result)