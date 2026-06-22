def reverse_string(s):
    return s[::-1]

def cycle_and_reverse(strings):
    for s in strings:
        reversed_s = reverse_string(s)
        print(reversed_s)

if __name__ == '__main__':
    sample_strings = ["Python", "is", "fun!"]
    cycle_and_reverse(sample_strings)