def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

if __name__ == '__main__':
    celsius_temp = 25
    fahrenheit_temp = 77
    
    print(f"{celsius_temp}C is {celsius_to_fahrenheit(celsius_temp):.2f}F")
    print(f"{fahrenheit_temp}F is {fahrenheit_to_celsius(fahrenheit_temp):.2f}C")