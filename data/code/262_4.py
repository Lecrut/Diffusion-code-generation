if __name__ == '__main__':
    numbers_str = "10 5 22 8 15"
    numbers = [int(x) for x in numbers_str.split()]
    if not numbers:
        print("No numbers provided.")
    else:
        smallest = min(numbers)
        largest = max(numbers)
        print(f"Smallest number: {smallest}")
        print(f"Largest number: {largest}")