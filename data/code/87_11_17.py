def test_combined_condition(x: int, y: int) -> bool:
    return x > 5 and y < 10

if __name__ == '__main__':
    result = test_combined_condition(6, 7)
    print(result)