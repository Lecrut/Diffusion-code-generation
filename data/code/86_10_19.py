result_map = {
    (True, True): 'Equal',
    (False, False): 'Equal',
    (True, False): 'Different',
    (False, True): 'Different'
}

def compare_booleans(a: bool, b: bool) -> str:
    return result_map[(a, b)]

if __name__ == '__main__':
    print(compare_booleans(True, True))
    print(compare_booleans(False, False))
    print(compare_booleans(True, False))
    print(compare_booleans(False, True))