if __name__ == '__main__':
    input_string = "Hello World"
    if isinstance(input_string, str):
        print(', '.join(input_string))
    else:
        print("Invalid input. Please provide a string.")