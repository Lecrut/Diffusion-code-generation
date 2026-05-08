def check_equivalence(a, b, c):
    return (a == b) and (a == c)
def structure_one(x):
    if x > 5:
        return "A"
    else:
        return "B"
def structure_two(x):
    if x >= 6:
        return "A"
    else:
        return "B"
def run_tests(test_cases):
    results = []
    for x in test_cases:
        result1 = structure_one(x)
        result2 = structure_two(x)
        equivalent = check_equivalence(result1, result2, x)
        results.append((x, result1, result2, equivalent))
    return results
if __name__ == '__main__':
    test_data = [3, 5, 6, 7, 10]
    test_results = run_tests(test_data)
    for x, res1, res2, eq in test_results:
        print(f"Input: {x}, Structure 1 Output: {res1}, Structure 2 Output: {res2}, Equivalent: {eq}")