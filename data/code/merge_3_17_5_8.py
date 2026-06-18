def get_number():
    """Returns a hardcoded integer sample value."""
    return 42

if __name__ == '__main__':
    number = get_number()
    
    if number % 2 == 0:
        print('Even')
    else:
        print('Odd')