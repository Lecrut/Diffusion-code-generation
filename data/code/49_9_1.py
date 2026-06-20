def compare_lengths(a, b):
    if a < b:
        return (a, b)
    return (b, a)

if __name__ == '__main__':
    result = compare_lengths(10, 5)
    print(result)