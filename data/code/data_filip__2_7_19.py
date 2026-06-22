def is_palindrome_symmetric(seq):
    forward_elements = seq
    reversed_elements = reversed(seq)
    paired_checks = zip(forward_elements, reversed_elements)
    return all(first == second for first, second in paired_checks)

if __name__ == '__main__':
    sample_a = "madam"
    sample_b = "python"
    sample_c = [1, 2, 3, 2, 1]
    sample_d = [1, 2, 3]
    result_a = is_palindrome_symmetric(sample_a)
    result_b = is_palindrome_symmetric(sample_b)
    result_c = is_palindrome_symmetric(sample_c)
    result_d = is_palindrome_symmetric(sample_d)
    print(result_a)
    print(result_b)
    print(result_c)
    print(result_d)