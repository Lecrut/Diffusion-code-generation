def sort_numbers(num1, num2):
    if num1 <= num2:
        return (num1, num2)
    else:
        return (num2, num1)

if __name__ == '__main__':
    result = sort_numbers(5, 3)
    print(result)