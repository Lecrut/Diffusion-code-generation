class DiamondRenderer:
    SIZE = 7

    @staticmethod
    def render_diamond():
        diamond = []
        center = (DiamondRenderer.SIZE - 1) // 2
        for i in range(DiamondRenderer.SIZE):
            row = [' '] * DiamondRenderer.SIZE
            for j in range(max(0, center - abs(i)), min(DiamondRenderer.SIZE, center + abs(i) + 1)):
                row[j] = '+'
            diamond.append(''.join(row))
        return '\n'.join(diamond)

if __name__ == '__main__':
    print(DiamondRenderer.render_diamond())