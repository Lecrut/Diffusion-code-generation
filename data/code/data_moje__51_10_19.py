def print_number_pyramid():
    height = 5
    for row in range(1, height + 1):
        numbers = list(range(1, row + 1))
        formatted_numbers = " ".join(f"{num:2}" for num in numbers)
        padding = " " * ((height - row) * 2)
        print(f"{padding}{formatted_numbers}")

if __name__ == '__main__':
    print_number_pyramid()