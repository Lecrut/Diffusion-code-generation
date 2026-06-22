class GridRenderer:
    SYMBOL = "+"
    
    @staticmethod
    def create_grid(rows, cols):
        row = GridRenderer.SYMBOL * cols + "\n"
        return "".join([row for _ in range(rows)])
    
if __name__ == '__main__':
    result = GridRenderer.create_grid(10, 10)
    print(result)