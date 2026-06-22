mixed_string = "Year2023: Temperature 25°C, Humidity 60%, ID 998877"

def extract_digits(text):
    return "".join(char for char in text if char.isdigit())

if __name__ == '__main__':
    result = extract_digits(mixed_string)
    print(result)