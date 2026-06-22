ComparisonResult = {
    True: "greater than",
    False: "less than"
}

def compare_integers(a, b):
    return ComparisonResult[a > b] if a != b else "equal to"

if __name__ == '__main__':
    result = compare_integers(15, 7)
    print(result)