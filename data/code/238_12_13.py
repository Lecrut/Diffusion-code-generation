class DiamondBox:
    def __init__(self):
        self.grid = [
            '   +   ',
            '  +++  ',
            ' ++++  ',
            '+++++++',
            ' ++++  ',
            '  +++  ',
            '   +   '
        ]

    def print_box(self):
        for row in self.grid:
            print(row)

if __name__ == '__main__':
    diamond = DiamondBox()
    diamond.print_box()