class MultiplicationGrid:
    START = 1
    END = 11

    @staticmethod
    def build():
        return [[row * col for col in range(MultiplicationGrid.START, MultiplicationGrid.END)] for row in range(MultiplicationGrid.START, MultiplicationGrid.END)]

    @staticmethod
    def format_output(grid):
        lines = []
        for row in grid:
            formatted_row = " ".join(f"{num:3}" for num in row)
            lines.append(formatted_row)
        return "\n".join(lines)

if __name__ == '__main__':
    grid_instance = MultiplicationGrid()
    result = MultiplicationGrid.build()
    print(MultiplicationGrid.format_output(result))