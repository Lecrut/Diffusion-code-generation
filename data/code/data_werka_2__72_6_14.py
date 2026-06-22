def compare_lists_with_zip(list_a, list_b):
    COMPARISON_SYMBOLS = {
        -1: "<",
        0: "==",
        1: ">"
    }
    results = []
    for val_a, val_b in zip(list_a, list_b):
        if val_a < val_b:
            diff = -1
        elif val_a > val_b:
            diff = 1
        else:
            diff = 0
        symbol = COMPARISON_SYMBOLS[diff]
        results.append(f"{val_a} {symbol} {val_b}")
    return results

if __name__ == '__main__':
    first_list = [10, 20, 30, 40]
    second_list = [10, 15, 35, 40]
    comparison_results = compare_lists_with_zip(first_list, second_list)
    for result in comparison_results:
        print(result)