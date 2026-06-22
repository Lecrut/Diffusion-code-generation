class ArrowheadGenerator:
    WIDTH = 5

    @staticmethod
    def generate_arrowhead():
        arrowhead = ""
        for i in range(1, ArrowheadGenerator.WIDTH + 1):
            arrowhead += " " * (ArrowheadGenerator.WIDTH - i) + "*" * (2 * i - 1) + "\n"
        return arrowhead

if __name__ == '__main__':
    print(ArrowheadGenerator.generate_arrowhead())