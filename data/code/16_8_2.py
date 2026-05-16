if __name__ == '__main__':
    sample_inputs = [
        "10",
        "-5",
        "0",
        "22.5",
        "-1"
    ]
    for line in sample_inputs:
        try:
            number = float(line.strip())
            if number > 0:
                print("Positive")
            else:
                print("Not Positive")
        except ValueError:
            print("Invalid Input")