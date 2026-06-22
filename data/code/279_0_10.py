class NumberIterator:
    START = 0
    END = 10

    @staticmethod
    def print_numbers():
        for i in range(NumberIterator.START, NumberIterator.END):
            print(i)

if __name__ == '__main__':
    NumberIterator.print_numbers()