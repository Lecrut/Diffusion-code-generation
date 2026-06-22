class LinePrinter:
    def __init__(self, data):
        self.data = data

    def print_lines(self):
        for line in self.data:
            print(line)

if __name__ == '__main__':
    sample_data = [
        "Hello World",
        "This is a test.",
        "Python scripting is fun.",
        "Optimal file handling matters."
    ]
    printer = LinePrinter(sample_data)
    printer.print_lines()