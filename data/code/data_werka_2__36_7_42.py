def reverse_string(s):

    def reverse_recursive(subs):
        if len(subs) <= 1:
            return subs
        else:
            return reverse_recursive(subs[1:]) + subs[0]
    return reverse_recursive(s)
if __name__ == '__main__':
    sample_string = 'Hello, 世界!'
    reversed_string = reverse_string(sample_string)
    print(reversed_string)