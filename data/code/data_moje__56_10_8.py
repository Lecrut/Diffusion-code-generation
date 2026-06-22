MULTIPLICAND = 5
TABLE_SIZE = 10

class MultiplicationTablePrinter:
    def __init__(self, base_number):
        self.base_number = base_number

    def compute_row(self, index):
        return self.base_number * index

    def display(self):
        for index in range(1, TABLE_SIZE + 1):
            product = self.compute_row(index)
            print(f"{self.base_number} x {index} = {product}")

if __name__ == '__main__':
    printer = MultiplicationTablePrinter(MULTIPLICAND)
    printer.display()