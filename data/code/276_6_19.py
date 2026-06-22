class IntegerRepeater:
    def __init__(self):
        self.repeated_list = []

    def read_and_repeat(self, filename, S):
        try:
            with open(filename, 'r') as f:
                numbers = [int(line.strip()) for line in f if line.strip().isdigit()]
                self.repeated_list = [num for num in numbers for _ in range(S)]
        except IOError as e:
            print(f"Error reading file {filename}: {e}", file=sys.stderr)

    def get_repeated_list(self):
        return self.repeated_list

if __name__ == '__main__':
    repeater = IntegerRepeater()
    repeater.read_and_repeat('sample.txt', 3)
    print(repeater.get_repeated_list())