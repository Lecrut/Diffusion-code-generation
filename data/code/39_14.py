def generate_substrings(s):
    n = len(s)
    for i in range(n):
        for j in range(i, n):
            yield s[i:j+1]
if __name__ == '__main__':
    input_string = "abc"
    substring_generator = generate_substrings(input_string)
    all_substrings = list(substring_generator)
    print(all_substrings)