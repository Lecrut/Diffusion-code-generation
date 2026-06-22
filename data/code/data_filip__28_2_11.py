def compress_run_length(text):
    if not text:
        return ""
    grouped = [[char, len(list(group))] for char, group in __import__('itertools').groupby(text)]
    return "".join([f"{count}{char}" for char, count in grouped])

if __name__ == '__main__':
    sample_data = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    result = compress_run_length(sample_data)
    print(result)