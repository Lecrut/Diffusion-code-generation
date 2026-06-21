def sort_two_floats(a, b):
    smaller = min(a, b)
    larger = max(a, b)
    return (smaller, larger)

if __name__ == '__main__':
    print(sort_two_floats(3.14, 2.71))