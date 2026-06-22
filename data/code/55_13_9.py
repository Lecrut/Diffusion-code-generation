def print_alphabet_triangle(n):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if n > len(alphabet):
        n = len(alphabet)
    for i in range(1, n + 1):
        line = alphabet[:i]
        print(line)

if __name__ == '__main__':
    sample_range = 5
    print_alphabet_triangle(sample_range)