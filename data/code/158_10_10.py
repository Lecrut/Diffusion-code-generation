if __name__ == '__main__':
    START = 0
    END = 50
    
    even_numbers = [num for num in range(START, END + 1) if num % 2 == 0]
    
    print(even_numbers)