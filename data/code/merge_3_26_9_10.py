# Lambda to compare two variables x and y returning True if x > y else False
compare = lambda x, y: x > y

if __name__ == '__main__':
    result1 = compare(5, 3)
    result2 = compare(4, 7)
    print(f"{result1=}") # Expected: result1=True
    print(f"{result2=}") # Expected: result2=False