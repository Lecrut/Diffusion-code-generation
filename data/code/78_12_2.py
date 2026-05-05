if __name__ == '__main__':
    month1 = 5
    month2 = 10
    if not isinstance(month1, int) or not isinstance(month2, int):
        print("Error: Inputs must be integers.")
    else:
        difference = abs(month1 - month2)
        print(difference)