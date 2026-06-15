if __name__ == '__main__':
    input_line = "10 5 20 8 15"
    numbers = input_line.split()
    if numbers:
        largest = max(map(int, numbers))
        print(largest)