def categorize_number(number):
    return ('low' if number < 30 else 'medium' if number < 60 else 'high')

if __name__ == '__main__':
    print(categorize_number(25))
    print(categorize_number(45))
    print(categorize_number(75))