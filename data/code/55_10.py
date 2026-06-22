def print_alphabet_triangle(height):
    if height <= 0:
        return
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(1, height + 1):
        limit = i if i < 26 else 26
        row_chars = alphabet[:limit]
        spaces = " " * (height - i)
        print(f"{spaces}{row_chars}")

if __name__ == '__main__':
    print_alphabet_triangle(10)