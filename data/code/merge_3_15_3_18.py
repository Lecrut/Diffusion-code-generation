x == y; x = 10; y = 20; print(x == y) if __name__ == '__main__' else None

# To make it a runnable module with proper structure as per instructions:

def check_equality(a, b):
    return bool(a == b)

if __name__ == "__main__":
    result = check_equality(10, 20)
    print(result)