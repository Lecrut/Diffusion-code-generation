def main():
    numbers = [10, 23, 45, 68, 91, 100]
    odd_generator = (num for num in numbers if num % 2 != 0)
    result_list = list(odd_generator)
    print("Odd numbers:", result_list)
if __name__ == '__main__':
    main()