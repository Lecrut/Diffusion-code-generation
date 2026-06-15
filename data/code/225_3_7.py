if __name__ == '__main__':
    input_data = [10, -5, 22, 0, -15, 30]
    if not input_data:
        print("Input list is empty")
    else:
        minimum = min(input_data)
        maximum = max(input_data)
        print(f"Minimum value: {minimum}")
        print(f"Maximum value: {maximum}")