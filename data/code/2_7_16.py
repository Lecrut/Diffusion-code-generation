def check_palindrome_symmetry(sequence):
    return all(a == b for a, b in zip(sequence, reversed(sequence)))

if __name__ == '__main__':
    sample1 = [1, 2, 3, 2, 1]
    sample2 = [1, 2, 3, 4]
    sample3 = "racecar"
    sample4 = "hello"
    print(check_palindrome_symmetry(sample1))
    print(check_palindrome_symmetry(sample2))
    print(check_palindrome_symmetry(sample3))
    print(check_palindrome_symmetry(sample4))