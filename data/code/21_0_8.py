def largest_of_three(a: int, b: int, c: int) -> int:
    return max(a, b, c)

if __name__ == '__main__':
    result = largest_of_three(10, 25, 15)
    print(result)