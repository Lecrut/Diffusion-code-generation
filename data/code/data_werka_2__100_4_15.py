def evaluate_greater(x: int, y: int) -> bool:
    if x > y:
        return True
    return False

if __name__ == '__main__':
    sample_x = 10
    sample_y = 5
    result = evaluate_greater(sample_x, sample_y)
    print(result)