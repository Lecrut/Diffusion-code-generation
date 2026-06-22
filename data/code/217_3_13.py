def max_without_conditional(a, b):
    return (a + b + abs(a - b)) // 2

if __name__ == '__main__':
    try:
        a = 5
        b = 3
        print(max_without_conditional(a, b))
    except Exception as e:
        print(f"An error occurred: {e}")