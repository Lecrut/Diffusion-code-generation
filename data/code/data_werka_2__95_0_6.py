CHECK_CATEGORIES = {
    "positive": lambda n: n > 0,
    "even": lambda n: n % 2 == 0,
    "divisible_by_three": lambda n: n % 3 == 0,
}

def analyze_number(n):
    results = {}
    for category_name, check_function in CHECK_CATEGORIES.items():
        results[category_name] = check_function(n)
    return results

if __name__ == '__main__':
    test_values = [6, 7, -2, 0, 15]
    for value in test_values:
        analysis = analyze_number(value)
        print(analysis)