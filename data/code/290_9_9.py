def pounds_to_ounces(pounds):
    if not isinstance(pounds, (int, float)):
        raise ValueError("Input must be an integer or float.")
    if pounds < 0:
        raise ValueError("Input must be non-negative.")
    return int(pounds * 16)

if __name__ == '__main__':
    print(pounds_to_ounces(5))
    print(pounds_to_ounces(10))