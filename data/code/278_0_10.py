class LinePrinter:
    @staticmethod
    def print_lines(data):
        for line in data:
            print(line)

if __name__ == '__main__':
    sample_data = [
        "Hello World",
        "This is a test.",
        "Python scripting is fun.",
        "Optimal file handling matters."
    ]
    LinePrinter.print_lines(sample_data)