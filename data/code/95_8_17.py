def check_positive_even_and_less_than_100(number):
    if number > 0 and number % 2 == 0 and number < 100:
        return True
    else:
        return False

if __name__ == '__main__':
    try:
        result1 = check_positive_even_and_less_than_100(42)
        print("Number is positive, even, and less than 100" if result1 else "Number does not meet the criteria")
        
        result2 = check_positive_even_and_less_than_100(55)
        print("Number is positive, even, and less than 100" if result2 else "Number does not meet the criteria")
        
        result3 = check_positive_even_and_less_than_100(-2)
        print("Number is positive, even, and less than 100" if result3 else "Number does not meet the criteria")
        
        result4 = check_positive_even_and_less_than_100(102)
        print("Number is positive, even, and less than 100" if result4 else "Number does not meet the criteria")
        
        result5 = check_positive_even_and_less_than_100(0)
        print("Number is positive, even, and less than 100" if result5 else "Number does not meet the criteria")
    except Exception as e:
        print(f"An error occurred: {e}")