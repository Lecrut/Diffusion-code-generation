class NumberAppender:
    START = 1
    END = 5

    @staticmethod
    def append_numbers():
        numbers = []
        for i in range(NumberAppender.START, NumberAppender.END + 1):
            numbers.append(i)
        return numbers

if __name__ == '__main__':
    result = NumberAppender.append_numbers()
    print(result)