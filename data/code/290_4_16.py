def pounds_to_kilograms(pounds):
    if pounds < 0:
        return 'Invalid input: weight cannot be negative.'
    elif pounds == 0:
        return 0.0
    else:
        kilograms = pounds * 0.45359237
        return round(kilograms, 1)
if __name__ == '__main__':
    print(pounds_to_kilograms(10))
    print(pounds_to_kilograms(0))
    print(pounds_to_kilograms(-5))