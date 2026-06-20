def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

if __name__ == '__main__':
    try:
        result_add = add(5, 3)
        result_subtract = subtract(10, 4)
        assert result_add == 8, f"Addition test failed: Expected 8, got {result_add}"
        assert result_subtract == 6, f"Subtraction test failed: Expected 6, got {result_subtract}"
        print(f"Addition of 5 and 3 is: {result_add}")
        print(f"Subtraction of 10 and 4 is: {result_subtract}")
    except AssertionError as e:
        print(e)