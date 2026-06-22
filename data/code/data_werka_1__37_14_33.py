class StringAccumulator:
    def __init__(self):
        self.result = ""

    def add(self, string):
        self.result += string

    def get(self):
        return self.result

if __name__ == '__main__':
    first_part = "Python"
    second_part = "Programming"
    accumulator = StringAccumulator()
    accumulator.add(first_part)
    accumulator.add(second_part)
    full_string = accumulator.get()
    print(full_string)