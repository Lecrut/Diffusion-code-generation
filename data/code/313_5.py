if __name__ == '__main__':
    input_string = "1 2 3 4 5 6 7 8 9 10"
    numbers = input_string.split()
    even_numbers = []
    for num_str in numbers:
        if num_str.isdigit():
            number = int(num_str)
            if number % 2 == 0:
                even_numbers.append(num_str)
    print("Even numbers found:", " ".join(even_numbers))