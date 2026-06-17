def calculate_average(*args):
    if not args:
        return 0
    return sum(args) / len(args)
if __name__ == '__main__':
    result1 = calculate_average(10, 20, 30)
    print(f"Average of (10, 20, 30): {result1}")
    result2 = calculate_average(5, 15, 25, 35)
    print(f"Average of (5, 15, 25, 35): {result2}")
    result3 = calculate_average()
    print(f"Average of (): {result3}")
    result4 = calculate_average(100)
    print(f"Average of (100): {result4}")