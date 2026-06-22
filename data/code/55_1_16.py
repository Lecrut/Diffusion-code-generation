def print_centered_alphabet_triangle(height: int) -> None:
    if height <= 0:
        return
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(1, height + 1):
        letters = alphabet[:i]
        pattern = " ".join(letters) + " " + " ".join(letters[::-1]) if i > 1 else letters
        width = 4 * height - 3
        padding = " " * ((width - len(pattern)) // 2)
        print(padding + pattern)

if __name__ == '__main__':
    sample_height = 7
    print_centered_alphabet_triangle(sample_height)