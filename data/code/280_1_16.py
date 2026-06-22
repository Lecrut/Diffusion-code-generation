class NumberAppender:
    MAX_NUMBER = 5

    @staticmethod
    def append_numbers() -> list:
        numbers = []
        for i in range(1, NumberAppender.MAX_NUMBER + 1):
            numbers.append(i)
        return numbers

if __name__ == '__main__':
    result = NumberAppender.append_numbers()
    print(result)