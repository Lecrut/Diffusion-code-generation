class TruthTableGenerator:
    INPUT_COUNT = 4
    LOGICAL_EXPRESSION = lambda A, B, C, D: (A and B) or (not C and D)

    @staticmethod
    def _get_headers(count):
        return [chr(ord('A') + i) for i in range(count)] + ['Result']

    @staticmethod
    def _get_separator(headers):
        width = 12
        parts = [width * '-' for _ in headers]
        return '+'.join(parts)

    def generate(self):
        headers = self._get_headers(self.INPUT_COUNT)
        print(' | '.join(f'{h:<{12}}' for h in headers))
        print(self._get_separator(headers))
        total = 2 ** self.INPUT_COUNT
        for i in range(total):
            values = []
            for j in range(self.INPUT_COUNT):
                bit = (i >> (self.INPUT_COUNT - 1 - j)) & 1
                values.append(bool(bit))
            result = self.LOGICAL_EXPRESSION(*values)
            row_strs = [str(v) for v in values] + [str(result)]
            print(' | '.join(f'{s:<{12}}' for s in row_strs))

if __name__ == '__main__':
    generator = TruthTableGenerator()
    generator.generate()