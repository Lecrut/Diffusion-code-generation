def compare_booleans(a: bool, b: bool) -> str:
    comparisons = {
        True: "True",
        False: "False"
    }
    result = comparisons[a] == comparisons[b]
    return f"{comparisons[a]} is equal to {comparisons[b]}" if result else f"{comparisons[a]} is not equal to {comparisons[b]}"

if __name__ == '__main__':
    a = True
    b = False
    print(compare_booleans(a, b))