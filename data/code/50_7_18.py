def build_star_triangle(row_count: int) -> str:
    if row_count < 1:
        return ""
    
    output_lines = []
    for current_row in range(1, row_count + 1):
        star_sequence = '*' * current_row
        output_lines.append(star_sequence)
    
    return '\n'.join(output_lines)

class TrianglePrinter:
    def __init__(self, limit: int):
        self.limit = limit

    def render(self) -> str:
        return build_star_triangle(self.limit)

if __name__ == '__main__':
    sample_height = 20
    triangle_data = build_star_triangle(sample_height)
    print(triangle_data)
    
    printer = TrianglePrinter(sample_height)
    alternative_output = printer.render()
    print()
    print(alternative_output)