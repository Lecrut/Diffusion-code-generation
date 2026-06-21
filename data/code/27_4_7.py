from functools import reduce

def rle_encode(s: str) -> str:
    if not s:
        return ""
    initial = (s[0], 1)
    result = reduce(
        lambda acc, char: (
            acc[0] + f"{acc[1]}" + char if acc[0] == char else acc[0] + f"{acc[1]}{char}",
            1
        ) if acc[0] != char else (
            acc[0],
            acc[1] + 1
        ),
        s[1:],
        initial
    )
    return result[0] + f"{result[1]}"

if __name__ == '__main__':
    print(rle_encode("XYZXYZ"))