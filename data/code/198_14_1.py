if __name__ == '__main__':
    input_line = "10 5 22 8 3"
    try:
        numbers = list(map(int, input_line.split()))
        if numbers:
            smallest = min(numbers)
            print(smallest)
        else:
            print("No numbers provided.")
    except ValueError:
        print("Error: Input must contain only space-separated integers.")