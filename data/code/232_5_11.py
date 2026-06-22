class SequencePrinter:
    def __init__(self):
        self.current = 0

    def next_number(self):
        number = self.current
        if number > 99:
            raise ValueError("Sequence limit exceeded")
        self.current += 1
        return number

if __name__ == '__main__':
    printer = SequencePrinter()
    while True:
        try:
            print(printer.next_number())
        except ValueError as e:
            break