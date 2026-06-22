class DiamondDrawer:
    ROWS = 5

    @staticmethod
    def draw_diamond():
        for i in range(DiamondDrawer.ROWS):
            spaces = ' ' * (DiamondDrawer.ROWS - abs(i) - 1)
            bars = '|' * (2 * abs(i) + 1)
            print(spaces + bars)

if __name__ == '__main__':
    DiamondDrawer.draw_diamond()