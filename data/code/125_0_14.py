def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

if __name__ == '__main__':
    try:
        result_add = add(15, 27)
        print(result_add)
        result_subtract = subtract(10, 4)
        print(result_subtract)
    except Exception as e:
        print(f"An error occurred: {e}")