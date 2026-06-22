class SequencePrinter:
    def __init__(self):
        self.current_number = 0

    def print_sequence(self):
        while self.current_number <= 99:
            print(self.current_number)
            self.current_number += 1

if __name__ == '__main__':
    printer = SequencePrinter()
    printer.print_sequence()