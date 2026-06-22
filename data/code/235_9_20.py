LINE_PATTERNS = {
    1: " *",
    2: "* *",
    3: "** **",
    4: "*** ***",
    5: "**** ****"
}

def generate_line_pattern(n):
    if n in LINE_PATTERNS:
        return LINE_PATTERNS[n]
    else:
        raise ValueError("Pattern not available for the given number")

if __name__ == '__main__':
    pattern = generate_line_pattern(3)
    print(pattern)