if __name__ == '__main__':
    sample_inputs = [
        "10",
        "-5",
        "0",
        "3.14",
        "-1.5"
    ]
    for line in sample_inputs:
        try:
            number = float(line.strip())
            if number > 0:
                print(f"{line}: Positive")
            else:
                print(f"{line}: Not Positive")
        except ValueError:
            print(f"{line}: Invalid input")