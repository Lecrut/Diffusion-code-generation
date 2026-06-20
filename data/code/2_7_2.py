def check_palindrome_symmetry(s):
    return all(a == b for a, b in zip(s, reversed(s)))

if __name__ == '__main__':
    sample_1 = "radar"
    sample_2 = "hello"
    print(check_palindrome_symmetry(sample_1))
    print(check_palindrome_symmetry(sample_2))