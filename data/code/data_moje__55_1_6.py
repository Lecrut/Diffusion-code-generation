def print_centered_alphabet_triangle(height: int) -> str:
    lines = []
    for i in range(1, height + 1):
        alphabet = "".join(chr(ord("A") + j) for j in range(i))
        repeated = "".join(ch * (i - j) for j, ch in enumerate(alphabet))
        line = repeated[:-1][::-1] + repeated
        lines.append(line.center(2 * height - 1))
    return "\n".join(lines)

if __name__ == "__main__":
    print(print_centered_alphabet_triangle(5))