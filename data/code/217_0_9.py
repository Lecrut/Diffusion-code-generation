def compare_integers(a, b):
    COMPARISON_MAP = {
        True: "greater than",
        False: "less than"
    }
    return COMPARISON_MAP[a > b] if a != b else "equal to"

if __name__ == '__main__':
    result = compare_integers(10, 5)
    print(result)