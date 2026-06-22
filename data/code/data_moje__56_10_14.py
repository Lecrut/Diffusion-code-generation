MULTIPLIER_TARGET = 5
OPERATION_LABELS = {
    1: "first",
    2: "second",
    3: "third",
    4: "fourth",
    5: "fifth",
    6: "sixth",
    7: "seventh",
    8: "eighth",
    9: "ninth",
    10: "tenth"
}

class MultiplicationTablePrinter:
    def __init__(self, base_number):
        self.base_number = base_number

    def get_line(self, index):
        label = OPERATION_LABELS.get(index, f"{index}-th")
        result = self.base_number * index
        return f"{self.base_number} multiplied by the {label} integer ({index}) equals {result}"

    def print_table(self):
        for i in range(1, 11):
            print(self.get_line(i))

if __name__ == '__main__':
    printer = MultiplicationTablePrinter(MULTIPLIER_TARGET)
    printer.print_table()