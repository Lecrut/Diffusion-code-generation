def hollow_square(n):
    if n <= 0:
        return ""
    if n == 1:
        return "*"
    top_bottom = "*" * n
    middle = "*" + " " * (n - 2) + "*"
    lines = [top_bottom]
    lines.extend([middle] * (n - 2))
    lines.append(top_bottom)
    return "\n".join(lines)

if __name__ == "__main__":
    result = hollow_square(5)
    print(result)