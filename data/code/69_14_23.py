class ListElementPrinter:
    def __init__(self, data):
        if not isinstance(data, list):
            raise ValueError("Input must be a list")
        self.data = data

    def print_elements(self):
        for index in range(len(self.data)):
            try:
                print(self.data[index])
            except IndexError as e:
                print(f"IndexError: {e}")

if __name__ == '__main__':
    sample_values = [1000, 2000, 3000, 4000, 5000]
    printer = ListElementPrinter(sample_values)
    printer.print_elements()