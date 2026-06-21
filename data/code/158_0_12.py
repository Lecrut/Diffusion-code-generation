if __name__ == '__main__':
    max_value = 50
    if not isinstance(max_value, int) or max_value < 1:
        raise ValueError("max_value must be a positive integer")
    
    even_numbers = [x for x in range(1, max_value + 1) if x % 2 == 0]
    print(even_numbers)