if __name__ == '__main__':
    input_data = [
        ("A", 10, 5),
        ("B", 20, 8),
        ("C", 15, 6)
    ]
    results = []
    for name, x, y in input_data:
        result = x + y
        results.append(f"{name}: {result}")
    for line in results:
        print(line)