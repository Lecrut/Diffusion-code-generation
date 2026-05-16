import sys
if __name__ == '__main__':
    num1 = 25
    num2 = 40
    if num1 > num2:
        difference = num1 - num2
        larger = f"{num1} is larger than {num2} by {difference}"
    elif num2 > num1:
        difference = num2 - num1
        larger = f"{num2} is larger than {num1} by {difference}"
    else:
        larger = f"{num1} and {num2} are equal"
    print(f"Comparison Report:")
    print(larger)