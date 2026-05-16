if __name__ == '__main__':
    month1 = 5
    month2 = 10
    if isinstance(month1, int) and isinstance(month2, int):
        difference = abs(month1 - month2)
        print(difference)
    else:
        print("Invalid input: Please enter integers.")