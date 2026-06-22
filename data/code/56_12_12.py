class MultiplicationTable:
    def __init__(self, base_number):
        self.base_number = base_number

    def generate_rows(self, count):
        if count < 1:
            return []
        lines = []
        for i in range(1, count + 1):
            lines.append(f"{self.base_number} x {i} = {self.base_number * i}")
        return lines

if __name__ == '__main__':
    table = MultiplicationTable(3)
    results = table.generate_rows(10)
    for line in results:
        print(line)