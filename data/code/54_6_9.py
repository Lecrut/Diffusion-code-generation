def hollow_square(n):
    if n <= 0:
        return ""
    if n == 1:
        return "*"
    row_full = "*" * n
    row_hollow = "*" + " " * (n - 2) + "*"
    rows = [row_full] + [row_hollow] * (n - 2) + [row_full]
    return "\n".join(rows)

if __name__ == "__main__":
    n = 5
    print(hollow_square(n))