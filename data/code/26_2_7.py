def main():
    # Hard-coded sample values to avoid interactive input
    num1 = 25
    num2 = 30
    
    print(f"Comparing {num1} and {num2}")
    
    if num1 > num2:
        result_text = f"{num1} is greater than {num2}"
    else:
        result_text = f"{num1} is not greater than {num2}"
        
    print(result_text)

if __name__ == '__main__':
    main()