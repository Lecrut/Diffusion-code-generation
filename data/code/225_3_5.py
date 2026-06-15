if __name__ == '__main__':
    input_data = [15, -3, 88, -102, 45, 0, 99]
    if not input_data:
        minimum = None
        maximum = None
    else:
        minimum = min(input_data)
        maximum = max(input_data)
    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")