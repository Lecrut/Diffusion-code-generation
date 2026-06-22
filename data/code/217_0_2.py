def compare_integers(a, b):
    comparison_map = {
        True: "greater than",
        False: "less than"
    }
    return comparison_map[a > b] if a != b else "equal to"

if __name__ == '__main__':
    result = compare_integers(10, 5)
    print(result)