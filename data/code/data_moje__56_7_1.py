def format_multiplication_table(base):
    width = len(str(base * 12)) + 2
    for multiplier in range(1, 13):
        result = base * multiplier
        print(f"{base} x {multiplier:>{width}} = {result:>{width}}")

if __name__ == '__main__':
    format_multiplication_table(7)