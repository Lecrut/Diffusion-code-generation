SAMPLE_STRINGS = ['hello', 'world', '!']

def reverse_strings(string_list):
    for s in string_list:
        print(s[::-1])
if __name__ == '__main__':
    reverse_strings(SAMPLE_STRINGS)