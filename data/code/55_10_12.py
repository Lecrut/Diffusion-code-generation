import string

def print_alphabet_triangle(height: int) -> None:
    alphabet = string.ascii_uppercase
    if height < 1 or height > len(alphabet):
        return
    for i in range(1, height + 1):
        row = ''.join((alphabet[j] for j in range(i)))
        print(row.center(height * 2 - 1))
if __name__ == '__main__':
    sample_height = 5
    print_alphabet_triangle(sample_height)