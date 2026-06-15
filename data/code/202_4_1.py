if __name__ == '__main__':
    input_line = "10 5 22 8 30"
    numbers = input_line.split()
    if numbers:
        largest = max(map(int, numbers))
        print(largest)