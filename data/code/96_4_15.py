def evaluate_expression(X: bool, Y: bool, Z: bool, W: bool) -> bool:
    part1 = X and Y
    part2 = Z and not W
    result = part1 or part2
    return result

if __name__ == '__main__':
    sample_result = evaluate_expression(True, False, True, False)
    print(sample_result)