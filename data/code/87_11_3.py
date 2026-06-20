def test_combined_conditions(x, y):
    return x > 5 and y < 10

if __name__ == '__main__':
    result = test_combined_conditions(6, 8)
    print(result)