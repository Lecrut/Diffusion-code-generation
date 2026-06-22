if __name__ == '__main__':
    numbers = [10.5, -3.2, 7.8, 0.0, -2.1, 4.9]
    
    if not numbers:
        print("No data")
    else:
        minimum = min(numbers)
        maximum = max(numbers)
        range_value = maximum - minimum
        print(f"Range: {range_value}")