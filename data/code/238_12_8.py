class DiamondRenderer:
    SIZE = 7

    @staticmethod
    def render_diamond():
        diamond = []
        for i in range(DiamondRenderer.SIZE):
            row = [' '] * DiamondRenderer.SIZE
            if i < DiamondRenderer.SIZE // 2 + 1:
                row[DiamondRenderer.SIZE // 2 - i] = '+'
                row[DiamondRenderer.SIZE // 2 + i] = '+'
            else:
                row[DiamondRenderer.SIZE // 2 - (i - DiamondRenderer.SIZE // 2)] = '+'
                row[DiamondRenderer.SIZE // 2 + (i - DiamondRenderer.SIZE // 2)] = '+'
            diamond.append(''.join(row))
        return '\n'.join(diamond)

if __name__ == '__main__':
    print(DiamondRenderer.render_diamond())