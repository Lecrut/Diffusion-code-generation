def get_multiplication_lines(number, start=1, end=10):
    if start > end:
        return []
    return [f"{number} x {i} = {number * i}" for i in range(start, end + 1)]

def format_table(number):
    lines = get_multiplication_lines(number)
    if not lines:
        return ""
    return "\n".join(lines)

if __name__ == '__main__':
    result = format_table(5)
    print(result)