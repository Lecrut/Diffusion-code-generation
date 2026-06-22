class CheckerboardGenerator:
    EMPTY = ' '
    FILLED = '#'

    @staticmethod
    def generate_checkerboard(rows, cols):
        board = []
        for r in range(rows):
            row_data = []
            for c in range(cols):
                if (r + c) % 2 == 0:
                    row_data.append(CheckerboardGenerator.EMPTY)
                else:
                    row_data.append(CheckerboardGenerator.FILLED)
            board.append(row_data)
        return board

    @staticmethod
    def format_checkerboard(board):
        formatted_board = []
        for row in board:
            formatted_row = ''.join(row)
            formatted_board.append(formatted_row)
        return '\n'.join(formatted_board)

if __name__ == '__main__':
    checkerboard_generator = CheckerboardGenerator()
    sample_board = checkerboard_generator.generate_checkerboard(5, 5)
    print(checkerboard_generator.format_checkerboard(sample_board))