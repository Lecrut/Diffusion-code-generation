class MultiplicationTableGenerator:
    BASE_NUMBER = 7
    LIMIT = 10

    @staticmethod
    def _format_line(factor: int, base: int) -> str:
        return f"{base} x {factor} = {base * factor}"

    def generate(self) -> str:
        factors = range(1, self.LIMIT + 1)
        return '\n'.join(self._format_line(f, self.BASE_NUMBER) for f in factors)

if __name__ == '__main__':
    generator = MultiplicationTableGenerator()
    print(generator.generate())