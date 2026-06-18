if __name__ == '__main__':
    numbers = [10, 20, 30, 40, 50]
    if not numbers:
        print("No numbers provided.")
    else:
        total = sum(numbers)
        count = len(numbers)
        mean = total / count
        print(f"The numbers entered are: {numbers}")
        print(f"The arithmetic mean is: {mean}")