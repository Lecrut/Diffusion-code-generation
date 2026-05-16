import sys
def main():
    numbers = [10, 20, 30, 40, 50]
    if not numbers:
        print("Error: The sequence of numbers is empty.")
        return
    first_number = numbers[0]
    last_number = numbers[-1]
    print(f"The sequence of numbers is: {numbers}")
    print(f"First number: {first_number}")
    print(f"Last number: {last_number}")
if __name__ == '__main__':
    main()