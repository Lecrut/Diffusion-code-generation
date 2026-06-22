class GrowingSequencePrinter:
    def __init__(self):
        self.current = 0

    def next_number(self):
        number = self.current
        self.current += 1
        return number

if __name__ == '__main__':
    printer = GrowingSequencePrinter()
    for _ in range(100):
        print(printer.next_number())