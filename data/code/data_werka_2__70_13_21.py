FIRST_CHAR_INDEX = 0
LAST_CHAR_INDEX = -1

def get_first_last(s):
    if not s:
        raise ValueError("String must not be empty")
    return (s[0], s[-1])

if __name__ == '__main__':
    test_string = "benchmark"
    result = get_first_last(test_string)
    print(result)