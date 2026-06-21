import itertools

def compress_run_length(s):
    result = []
    for char, group in itertools.groupby(s):
        count = sum(1 for _ in group)
        if count > 1:
            result.append(f"{char}{count}")
        else:
            result.append(char)
    return "".join(result)

if __name__ == '__main__':
    sample = "AAABBBCCD"
    print(compress_run_length(sample))