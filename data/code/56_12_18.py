class MultiplicationTable:
    def __init__(self, base):
        self.base = base

    def get_first_n_rows(self, count):
        output = []
        for i in range(1, count + 1):
            product = self.base * i
            output.append(f"{self.base} x {i} = {product}")
        return output

if __name__ == '__main__':
    table_instance = MultiplicationTable(3)
    lines = table_instance.get_first_n_rows(10)
    for line in lines:
        print(line)