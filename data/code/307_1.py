import sys
def repeat_string(s: str, n: int) -> str:
    if n <= 0:
        return ""
    return s * n
if __name__ == '__main__':
    test_string = "abc"
    test_n = 3
    result = repeat_string(test_string, test_n)
    print(result)