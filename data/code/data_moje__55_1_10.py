import string

def print_centered_alphabet_triangle(height: int) -> None:
    alphabet = string.ascii_uppercase
    max_width = height + (height - 1)
    for i in range(1, height + 1):
        letters = alphabet[:i]
        row_letters = "".join(letters[i::-1] + letters[1:])
        print(row_letters.center(max_width))

if __name__ == '__main__':
    sample_height = 5
    print_centered_alphabet_triangle(sample_height)