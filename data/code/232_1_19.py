def growing_sequence(limit):
    return (x for x in range(1, limit + 1))

class SequencePrinter:
    @staticmethod
    def print_sequence(limit):
        generator = growing_sequence(limit)
        while True:
            try:
                number = next(generator)
                print(number)
            except StopIteration:
                break

if __name__ == '__main__':
    sequence_printer = SequencePrinter()
    sequence_printer.print_sequence(10)