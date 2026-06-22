def build_diamond(size: int) -> str:
    if size <= 0:
        return ""
    
    lines = []
    for i in range(size):
        spaces = " " * (size - 1 - i)
        stars = "*" * (2 * i + 1)
        lines.append(spaces + stars)
    
    for i in range(size - 2, -1, -1):
        spaces = " " * (size - 1 - i)
        stars = "*" * (2 * i + 1)
        lines.append(spaces + stars)
    
    return "\n".join(lines)

class DiamondPrinter:
    def __init__(self, size: int):
        self.size = size

    def get_pattern(self) -> str:
        return build_diamond(self.size)

if __name__ == "__main__":
    sample_size = 5
    result = build_diamond(sample_size)
    print(result)
    
    printer = DiamondPrinter(sample_size)
    print(printer.get_pattern())