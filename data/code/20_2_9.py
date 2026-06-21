NUMBERS_TO_LABELS = {
    0: "zero",
    2: "two",
    4: "four",
    6: "six",
    8: "eight",
    10: "ten",
    12: "twelve",
}

def check_even(number: int) -> bool:
    if number in NUMBERS_TO_LABELS:
        return True
    return number % 2 == 0

if __name__ == "__main__":
    test_values = [1, 2, 3, 8, 9, 12, 15, 20]
    for value in test_values:
        result = check_even(value)
        print(result)