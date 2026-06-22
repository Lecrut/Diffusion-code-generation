from itertools import groupby

def compress_run_length(seq):
    return ''.join(
        f"{char}{sum(1 for _ in group)}" 
        for char, group in groupby(seq)
    )

if __name__ == '__main__':
    test_string = "aaabbcdddda"
    result = compress_run_length(test_string)
    print(result)