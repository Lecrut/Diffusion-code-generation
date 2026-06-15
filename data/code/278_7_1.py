import sys
def print_strings_fast(string_list):
    sys.stdout.write('\n'.join(string_list) + '\n')
if __name__ == '__main__':
    sample_list = ["hello", "world", "python", "speed"]
    print_strings_fast(sample_list)