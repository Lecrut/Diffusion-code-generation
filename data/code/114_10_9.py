def multiply_numbers(a, b):
    return a * b

if __name__ == '__main__':
    results = {
        "5*10": multiply_numbers(5, 10),
        "10*5": multiply_numbers(10, 5),
        "-3*7": multiply_numbers(-3, 7)
    }
    
    for key, value in results.items():
        print(f"{key} = {value}")