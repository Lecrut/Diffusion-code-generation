class AsciiArt:
    def generate_triangle(self, base):
        return '\n'.join('*' * i for i in range(1, base + 1))

if __name__ == '__main__':
    art = AsciiArt()
    triangle_art = art.generate_triangle(10)
    print(triangle_art)