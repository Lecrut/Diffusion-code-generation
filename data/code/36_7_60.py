def reverse_string(s):
    def reverse_iterative(subs):
        reversed_chars = []
        for char in subs:
            reversed_chars.append(char)
        return ''.join(reversed_chars[::-1])
    return reverse_iterative(s)

if __name__ == '__main__':
    sample_string = "Hello, 世界!"
    reversed_string = reverse_string(sample_string)
    print(reversed_string)