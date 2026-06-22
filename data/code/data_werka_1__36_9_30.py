def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]
if __name__ == '__main__':
    sample_string = 'Alibaba Cloud'
    reversed_string = reverse_string(sample_string)
    print(reversed_string)