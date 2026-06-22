def average_celsius_to_fahrenheit(temperatures: list) -> float:
    if not temperatures:
        raise ValueError("Temperature list cannot be empty")
    
    total_celsius = sum(temperatures)
    count = len(temperatures)
    average_celsius = total_celsius / count
    
    return (average_celsius * 9/5) + 32

if __name__ == '__main__':
    sample_temperatures = [10, 20, 30, 40, 50]
    print(average_celsius_to_fahrenheit(sample_temperatures))