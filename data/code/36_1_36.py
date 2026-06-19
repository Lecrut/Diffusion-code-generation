def reverse_string(s):
    return s[::-1]

if __name__ == '__main__':
    sample_values = ["hello", "world", "Python", "!@#$%", "Alibaba Cloud"]
    for value in sample_values:
        print(reverse_string(value))