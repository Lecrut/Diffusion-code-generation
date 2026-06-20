def subtract(a, b):
    return a - b

if __name__ == '__main__':
    try:
        print(subtract(10, 5))
        print(subtract(5, 10))
        print(subtract(10, 10))
        print(subtract(-5, 3))
        print(subtract(3, -5))
        print(subtract(-10, -5))
        print(subtract(-10, -10))
    except Exception as e:
        print(f"An error occurred: {e}")