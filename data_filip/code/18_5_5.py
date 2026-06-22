def run_length_encode(input_string):
    if not input_string:
        return ""
    result = [(char, sum(1 for _ in group)) for char, group in __import__('itertools').groupby(input_string)]
    return "".join(f"{count}{char}" if count > 1 else char for char, count in result)

if __name__ == '__main__':
    print(run_length_encode("aabcccccaaa"))
    print(run_length_encode("abc"))
    print(run_length_encode(""))
    print(run_length_encode("a"))