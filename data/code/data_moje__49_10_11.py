def _validate_side_length(value: int) -> None:
    if not isinstance(value, int):
        raise TypeError("Side length must be an integer.")
    if value <= 0:
        raise ValueError("Side length must be a positive integer.")

def _generate_row_string(side_length: int) -> str:
    return "*" * side_length

def print_star_square(side_length: int = 5) -> str:
    _validate_side_length(side_length)
    row = _generate_row_string(side_length)
    lines = [row for _ in range(side_length)]
    result = "\n".join(lines)
    print(result)
    return result

class StarSquarePrinter:
    def __init__(self, side_length: int) -> None:
        self._side_length = side_length
        _validate_side_length(side_length)

    def get_pattern(self) -> str:
        row = "*" * self._side_length
        lines = [row for _ in range(self._side_length)]
        return "\n".join(lines)

    def display(self) -> str:
        pattern = self.get_pattern()
        print(pattern)
        return pattern

if __name__ == '__main__':
    print_star_square(5)
    printer = StarSquarePrinter(5)
    print(printer.display())