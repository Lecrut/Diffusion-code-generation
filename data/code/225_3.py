if __name__ == '__main__':
    input_data = [10, -5, 22, 0, -15, 33]
    if not input_data:
        minimum = None
        maximum = None
    else:
        minimum = min(input_data)
        maximum = max(input_data)
    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")