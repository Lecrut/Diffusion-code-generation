def reverse_string(s):
    return s[::-1]

if __name__ == '__main__':
    sample_values = ["hello", "world", "Python", "!@#$%", "12345"]
    for value in sample_values:
        print(reverse_string(value))