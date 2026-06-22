class RightAngledTriangle:
    @staticmethod
    def generate_line_pattern(n):
        return '\n'.join(['*' * (i + 1) for i in range(n)])

if __name__ == '__main__':
    print(RightAngledTriangle.generate_line_pattern(5))