class HollowAlphabetTriangle:
    def __init__(self, base_width: int):
        self.base_width = base_width
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def generate(self) -> str:
        if self.base_width < 1:
            return ""
        lines = []
        for row in range(1, self.base_width + 1):
            line_parts = []
            for col in range(1, row + 1):
                is_hollow_boundary = (
                    row == 1 or
                    row == self.base_width or
                    col == 1 or
                    col == row
                )
                if is_hollow_boundary:
                    char_code = col - 1
                    if char_code >= 26:
                        char_code = char_code % 26
                    line_parts.append(self.alphabet[char_code])
                else:
                    line_parts.append(" ")
            lines.append(" ".join(line_parts))
        return "\n".join(lines)

if __name__ == '__main__':
    sample_width = 7
    triangle = HollowAlphabetTriangle(sample_width)
    output = triangle.generate()
    print(output)