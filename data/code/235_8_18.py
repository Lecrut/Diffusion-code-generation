class ArrowheadGenerator:
    WIDTH = 5

    @staticmethod
    def generate_arrowhead():
        result = ""
        for i in range(1, ArrowheadGenerator.WIDTH + 1):
            result += " " * (ArrowheadGenerator.WIDTH - i) + "*" * (2 * i - 1) + "\n"
        return result

if __name__ == '__main__':
    arrowhead_pattern = ArrowheadGenerator.generate_arrowhead()
    print(arrowhead_pattern)