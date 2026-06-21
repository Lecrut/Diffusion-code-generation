def get_even_numbers():
    even_numbers = []
    for number in range(100):
        if number & 1 == 0:
            even_numbers.append(number)
    return sorted(even_numbers)

if __name__ == '__main__':
    sample_values = [42, 7, 0, -15, "hello", 3.14]
    for value in sample_values:
        if isinstance(value, int):
            print(f"{value} is even" if value & 1 == 0 else f"{value} is odd")
        else:
            print("Error: Input must be an integer.")
    
    even_numbers = get_even_numbers()
    print(even_numbers)