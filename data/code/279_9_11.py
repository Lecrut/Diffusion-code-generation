if __name__ == '__main__':
    numbers = range(1, 101)
    divisible_by_3_and_5 = {i for i in numbers if i % 3 == 0 and i % 5 == 0}
    
    print(divisible_by_3_and_5)