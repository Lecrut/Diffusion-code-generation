def longest_string(strings):
    return max(strings, key=len)

if __name__ == '__main__':
    sample_strings = ["short", "longer string", "longest string of all"]
    print(longest_string(sample_strings))