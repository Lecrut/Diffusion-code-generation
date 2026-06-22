def add_numbers(a, b):
    try:
        result = float(a) + float(b)
        return result
    except ValueError as e:
        return f"Error: {e}"

if __name__ == '__main__':
    sample_values = [
        (5, 10),
        ("20", "22"),
        ("five", 3),
        (7.5, 2.5)
    ]
    
    for a, b in sample_values:
        print(add_numbers(a, b))