def reverse_string(s):
    reversed_s = ""
    for i in range(len(s) - 1, -1, -1):
        reversed_s += s[i]
    return reversed_s
if __name__ == '__main__':
    sample_string = "hello"
    reversed_result = reverse_string(sample_string)
    print(reversed_result)