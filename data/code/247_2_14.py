def add(a, b):
    try:
        return int(a) + int(b)
    except ValueError:
        return "Error: Invalid input types"

if __name__ == '__main__':
    print(add(10, 5))
    print(add("3", 2))
    print(add(4.5, 2))
    print(add("hello", 1))
    print(add(10, "text"))