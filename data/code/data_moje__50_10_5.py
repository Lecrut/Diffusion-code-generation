import sys

def generate_star_triangle(height: int) -> str:
    if height <= 0:
        return ""
    lines = []
    for i in range(1, height + 1):
        lines.append("*" * i)
    return "\n".join(lines)

if __name__ == "__main__":
    sample_height = 5
    result = generate_star_triangle(sample_height)
    print(result)