from itertools import groupby

def compress_run_length(sequence):
    return ''.join(
        f"{char}{len(list(group))}" if len(list(group)) > 1 else char
        for char, group in groupby(sequence)
    )

if __name__ == '__main__':
    test_string = "AAABBBCCCD"
    print(compress_run_length(test_string))