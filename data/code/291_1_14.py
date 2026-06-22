def find_shorter_length(length1: float, length2: float) -> str:
    shorter = min(length1, length2)
    return f"{shorter} cm"

if __name__ == '__main__':
    length_a = 35.7
    length_b = 42.1
    result = find_shorter_length(length_a, length_b)
    print(result)

    length_c = 80.0
    length_d = 60.0
    result2 = find_shorter_length(length_c, length_d)
    print(result2)