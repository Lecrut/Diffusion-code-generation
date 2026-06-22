class CubeVolumeCalculator:
    def calculate(self, edge_length):
        return edge_length * edge_length * edge_length

if __name__ == '__main__':
    calculator = CubeVolumeCalculator()
    print(calculator.calculate(5))
    print(calculator.calculate(10))
    print(calculator.calculate(3.5))