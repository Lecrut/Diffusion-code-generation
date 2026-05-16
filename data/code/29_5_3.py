def reverse_string_iterative(s):
    n = len(s)
    reversed_s = []
    for i in range(n):
        reversed_s.append(s[n - 1 - i])
    return "".join(reversed_s)
if __name__ == '__main__':
    sample_string = "hello"
    reversed_result = reverse_string_iterative(sample_string)
    print(reversed_result)
    sample_string_2 = "world"
    reversed_result_2 = reverse_string_iterative(sample_string_2)
    print(reversed_result_2)
    sample_string_3 = "python"
    reversed_result_3 = reverse_string_iterative(sample_string_3)
    print(reversed_result_3)